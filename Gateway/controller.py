"""! @brief Главный шлюз для связи микросервисов."""

from flask import Flask, request, render_template
from flask_cors import CORS
import requests
import base64
import json
import pickle

from service.Image import *

from service.ResponseHandlers import *
from service.exceptions.GatewayExceptions import *
from config.configurations import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, resources={r"/api/*": {"origins": "*"}})

class GatewayServiceAPI:
    """! Класс предоставляющий API шлюза.
    Данный класс предоставляет необходимое API для обращения к микросервисам.
    """

    def detect_letters(self, img):
        """! Отправляет запрос на микросервис детекции.
        @throw GatewayServiceException возникла внутренняя ошибка сервиса
        @return ответ микросервиса детекции.
        """
        img_bytes = pickle.dumps(img)
        jstr = json.dumps({"image": base64.b64encode(img_bytes).decode('ASCII')})

        headers = {'Content-type': 'application/json', 'Accept': 'text/'}
        try:
            r = requests.post(Config.DETECTION_ENDPOINT,
                            data=jstr,
                            headers=headers)
        except requests.exceptions.RequestException:
            raise GatewayServiceException("Сервис недоступен", name="Detection error: детекция", status_code=503)

        return r

    def recognize_letters(self, letters):
        """! Отправляет запрос на микросервис нейронной сети.
        @throw GatewayServiceException возникла внутренняя ошибка сервиса
        @return ответ микросервиса нейронной сети.
        """
        image_converter = ImageConverter()
        
        letters_img_bytes = image_converter.image_to_bytes(letters)

        jstr = json.dumps({"letters": letters_img_bytes})

        headers = {'Content-type': 'application/json', 'Accept': 'text/'}
        try:
            r = requests.post(Config.NEURAL_NETWORK_ENDPOINT,
                            data=jstr,
                            headers=headers)
        except requests.exceptions.RequestException:
            raise GatewayServiceException("Сервис недоступен", name="Recognition error", status_code=503)

        return r


    def create_font(self, letters, letters_recognized):
        """! Отправляет запрос на микросервис создания шрифта.
        @throw GatewayServiceException возникла внутренняя ошибка сервиса
        @return ответ микросервиса создания шрифта.
        """
        image_converter = ImageConverter()
        
        letters_img_bytes = image_converter.image_to_bytes(letters)
        letters_ascii = [[letters_img_bytes[i], letters_recognized[i]] for i in range(len(letters))]

        jstr = json.dumps({"letters_ascii": letters_ascii})

        headers = {'Content-type': 'application/json', 'Accept': 'text/'}
        try:
            r = requests.post(Config.FONT_CREATION_ENDPOINT,
                            data=jstr,
                            headers=headers)
        except requests.exceptions.RequestException:
            raise GatewayServiceException("Сервис недоступен", name="Font creation error", status_code=503)

        return r
    
gateway = GatewayServiceAPI()

@app.route('/api/v1/gateway/upload', methods=['POST'])
def upload():
    """! Обработка POST-запроса загрузки файла.
    Получает на вход картинку с изображениями глифов. 
    Далее отправляет на микросервис детекции. 
    Результат детекции отправляется микросервису нейронной сети.
    Результат нейронной сети отпарвляется микросервису создания шрифта.
    Результат микросервиса создания шрифта возвращается в качастве результата. 
    @return ответ микросервиса создания шрифта.
    """
    det_resp_handler = DetectionRespHandler(app.config)
    recog_resp_handler = RecognitionRespHandler(app.config)
    font_resp_handler = FontCreationRespHandler(app.config)

    try:
        #Get image with alphabet from frontend
        image_file = request.files['file'].read()
        image = Image(image_file, app.config)
    
        #Detection
        det_resp = gateway.detect_letters(image.img)
        #letters - array of letters images (numpy.ndarray)
        letters = det_resp_handler.get_letters(det_resp)
        
        #Recognition
        recog_resp = gateway.recognize_letters(letters)
        #letters_recognized - array of ASCII codes
        letters_recognized = recog_resp_handler.get_recognized_letters(recog_resp)
        
        #Font creation
        font_resp = gateway.create_font(letters, letters_recognized)
        font_file = font_resp_handler.get_font_file(font_resp)
            
    except GatewayServiceException as gse:
        error = str(gse.status_code) + ": " + gse.message
        return error

    return font_file.content

        
    
