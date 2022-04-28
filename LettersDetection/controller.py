from flask import Flask, request
import base64
import json
import pickle

from service.FileConverter import *
from service.Image import *
from service.LettersExtractor import *
from config.configurations import Config

app = Flask(__name__)

@app.route('/api/v1/detection/detect_letters', methods=['POST'])
def detect_letters():
    config = Config()

    if request.json.get("image") == None:
        return "", 400
    
    input_image = pickle.loads(base64.b64decode(request.json['image']))

    #Parse image
    image = Image(config)
    img_erode, gray = image.image_convert(input_image)

    #Get an array of letters
    letters_extractor = LettersExtractor(config)
    letters_extractor.letters_extract(input_image, img_erode, gray)                           
    letters_extractor.letters_sort_X()

    letters_output = []

    #letters_extractor.letters[i][2] - letter's image as numpy.ndarray 
    for i in range(len(letters_extractor.letters)):
        letters_output.append(letters_extractor.letters[i][2].tolist())
    resp = json.dumps({"letters" : letters_output})
    return resp


