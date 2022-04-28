"""! @brief Классы для работы с изображениями."""

import cv2
import numpy as np
import base64
import pickle
import matplotlib.pyplot as plt

class Image:
    """! Класс для конвертации изображения.
    Данный класс предоставляет необходимы функционал для конвертации изображения.
    """

    def __init__(self, image_file, config):
        """! Конструктор класса для преобразования сохранения массива байтов в виде фотографий."""
        self.img = cv2.imdecode(np.fromstring(image_file, np.uint8), cv2.IMREAD_COLOR)
        self.config = config

    def image_save(self, letters):
        """! Преобразует массив байтов в изображения.
        Данный метод предоставляет возожность преобразования 
        массива байтов в изображения и последующего его сохранения. 
        @param letters массив байтов изобрадений глифов. 
        """
        for i in range(len(letters)):
            number = str(i)
            if i < 10:
                number = '0' + number
            path = self.config["PNG_PATH"] +\
                self.config["FILE_NAME"] +\
                number +\
                self.config["PNG_EXTENSION"]
            plt.imsave(path, letters[i])


class ImageConverter:
    """! Класс для конвертации изображения.
    Данный класс предоставляет необходимы функционал для конвертации изображения.
    """
    
    def __init__(self):
        """! Конструктор класса для преобразования изображения в массив байтов."""
        pass

    def image_to_bytes(self, images):
        """! Преобразует изображение в массив байтов.
        Преобразует картинки в массив кодированных байтов.
        @param images масив np.ndarray изображений 
        @return массив байтов
        """
        images_bytes = []

        for i in range(len(images)):
            img_bytes = pickle.dumps(images[i])
            img_b64encode = base64.b64encode(img_bytes).decode('ASCII')
            images_bytes.append(img_b64encode)

        return images_bytes

        

