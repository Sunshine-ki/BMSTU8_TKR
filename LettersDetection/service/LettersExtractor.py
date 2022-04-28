"""! @brief Распознание ."""

import cv2
import numpy as np
import matplotlib.pyplot as plt

class LettersExtractor:
    """! Класс для обрезания изображений"""

    def __init__(self, config):
        """! Конструктор класса LettersExtractor, инициализирующий конфигурацию."""
        self.letters = []
        self.config = config

    
    def letters_extract(self, img_prev, img_erode, gray):
        """! Вырезает глифы на картинке.
        @param img_prev исходная картинка
        @param img_erode сегментированнная картинка
        @param gray картинка с изменном фоном
        @return список нарезанных картинок в форате np.ndarray.
        """
        # Get contours
        contours, hierarchy = cv2.findContours(img_erode, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        for idx, contour in enumerate(contours):
            (x_prev, y_prev, w_prev, h_prev) = cv2.boundingRect(contour)
            x = x_prev 
            y = y_prev - 2
            w = w_prev
            h = h_prev + 2
            if hierarchy[0][idx][3] == 0:
                cv2.rectangle(img_prev, (x, y), (x + w, y + h), (70, 0, 0), 1)
                letter_crop = gray[y:y + h, x:x + w]

                # Resize letter canvas to square
                size_max = max(w, h)
                #print(size_max)
                letter_square = 255 * np.ones(shape=[size_max, size_max], dtype=np.uint8)
                if w > h:
                    y_pos = size_max//2 - h//2 
                    letter_square[y_pos:y_pos + h, 0:w] = letter_crop
                elif w < h:
                    # Enlarge image left-right
                    x_pos = size_max//2 - w//2 
                    letter_square[0:h, x_pos:x_pos + w] = letter_crop
                else:
                    letter_square = letter_crop

                # Resize letter to 28x28 and add letter and its X-coordinate
                self.letters.append((x, w, letter_square))


    def letters_sort_X(self):
        """! Сортирует картинки по горизонтали.
        @return список отсортированных по горизонтали картинок в форате np.ndarray.
        """
        # Sort array in place by X-coordinate
        self.letters.sort(key=lambda x: x[0])
