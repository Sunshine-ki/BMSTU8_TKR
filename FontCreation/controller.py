"""! @brief Определение микросервиса для создания шрифта из набора глифов."""
##
# @file fontCreator.py
#
# Copyright (c) 2020 Sunshine-ki.
from flask import Flask, request, send_file
from flask_cors import CORS

import base64
import json
import pickle
import matplotlib.pyplot as plt

from service.fontCreator import *
from model.fontModel import *
from config.constants import GLYPHS_PATH, PNG

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/v1/font_creator', methods=['POST'])
def font_creator():
    """! Создает шрифт из набора глифов.
    Генерирует ttf-шрифт на основе переданных глифов в теле POST-запроса. 
    @return сгенерированный шрифт из переданных глифов, или ошибка 400 в случае отсутствия глифов в теле запроса.
    """
    print("font_creator --> post")

    letters_ascii = request.json["letters_ascii"]
    if letters_ascii == None:
        err_msg = "No letters_ascii :("
        print(err_msg)
        return err_msg, 400

    letters_count = len(letters_ascii)
    letters_img = [pickle.loads(base64.b64decode(letters_ascii[i][0])) for i in range(letters_count)]
    ascii_codes = [letters_ascii[i][1] for i in range(letters_count)]

    for i in range(letters_count):
        if ascii_codes[i] != "0":
            path = GLYPHS_PATH + ascii_codes[i] + "." + SVG
            plt.imsave(path, letters_img[i])

    font = fontCreator()
    font.create(fontModel())
    print("success post")
    return send_file(FONT_FILE_NAME)


@app.route('/api/v1/font_creator', methods=['GET'])
def font_creator_get():
    """! Создает шрифт из набора глифов.
    Генерирует ttf-шрифт на основе переданных глифов в теле POST-запроса. 
    @return сгенерированный шрифт из переданных глифов, или ошибка 400 в случае отсутствия глифов в теле запроса.
    """
    print("font_creator --> get")
    return send_file(FONT_BASE_NAME)
