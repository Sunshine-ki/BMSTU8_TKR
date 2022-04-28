"""! @brief Конфигурация для Gateway."""

class Config(object):
    #URI
    ## Путь до микросервиса детекции 
    DETECTION_ENDPOINT = "http://anasvicar01.pythonanywhere.com/api/v1/detection/detect_letters"
    ## Путь до микросервиса нейронной сети
    NEURAL_NETWORK_ENDPOINT = "http://neuralnetworktkr22.pythonanywhere.com/api/v1/recognition/recognize_letters"
    ## Путь до микросервиса создания шрифта
    FONT_CREATION_ENDPOINT = "http://67.205.130.22:5001/api/v1/font_creator"
    
    #All paths
    PNG_PATH = 'image/png/'

    #All extensions
    ## Имя папки, содерж. изображения 
    FILE_NAME = 'img'
    ## Расширение для растрового файла
    PNG_EXTENSION = '.png'
    
    
    



