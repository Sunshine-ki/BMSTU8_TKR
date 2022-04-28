"""! @bсrief Определение класса для конвертации cv2."""

import cv2
import numpy as np
import matplotlib.pyplot as plt

class Image:
    """! Класс для подготовки изображения для дальнейшего распознования.
    Данный класс предоставляет необходимы функционал для
    подготовки изображения для дальнейшего распознования.
    """
     
    def __init__(self, config):
        """! Конструктор класса Image, инициализирующий конфигурацию."""
        self.config = config

    def image_convert(self, img):
        """! Изменяет фон, обрезает изображение
        @param img изображение представленное в np.ndarray
        @return ответ микросервиса создания шрифта.
        """
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)
        img_erode = cv2.erode(thresh, np.ones((3, 3), np.uint8), iterations=1)

        return img_erode, gray

