"""! @brief Определение класса для работы со шрифтом."""
##
# @file fontCreator.py
#
# Copyright (c) 2020 Sunshine-ki.
from os import listdir
from os.path import isfile
from os.path import join as joinpath
from socket import INADDR_ALLHOSTS_GROUP
import fontforge

from config.constants import *
import model.fontModel as fontModel

class fontCreator:
    """! Класс для работы со шрифтом.
    Данный класс предоставляет весь необходимы функционал для создания шрифта.
    """

    def __init__(self):
        """! Конструктор класса для работы со шрифтом.
        @return экземпляр класса fontCreator с инициализированным шрифтом.
        """
        ## Результурующий шрифт.
        self.__font = fontforge.font()

        self.all_glyphs = list()
        self.all_glyphs.extend(range(48,58)) # [48 - 57]  : [0-9]
        self.all_glyphs.extend(range(65,91)) # [65 - 90]  : [A-Z]
        self.all_glyphs.extend(range(97,123)) # [97 - 122] : [a-z]


    def create(self, font_model: fontModel, dir: str = "glyphs", result_name: str = FONT_FILE_NAME):
        """! Создает шрифт
        Генерирует ttf-шрифт на основе переданных глифов и метаданных. 
        Все недостающие глифы будут заменены базовыми.
        @param font_model метаданные о шрифте
        @param dir директория, в которой расположены глифы
        @param result_name имя результирующего файла-шрифта
        """
        images = filter(lambda x: x.endswith(SVG), listdir(dir))
        existing_glyphs = list()

        # Вставляем существующие глифы (которые пришли от пользователя)
        for img in images:
            num = int(img.split('.')[0])
            existing_glyphs.append(int(num))
            path = joinpath(dir, img)
            print(num, path)
            glyph = self.__font.createMappedChar(num)
            glyph.importOutlines(path)

        # Вставляем недостающие глифы
        need_glyphs = list(set(self.all_glyphs) - set(existing_glyphs))
        base_font = fontforge.open(FONT_BASE_NAME)               
        for glyph_number in need_glyphs:
            base_font.selection.select(("unicode",None), glyph_number)    # Выбираем нужный глиф
            base_font.copy()                                              # Копируем выбранный глиф в буфер обмена.

            self.__font.selection.select(("unicode",None), glyph_number)      
            self.__font.paste()                                           # Вставляем выбранный глиф из буфера.

        self.__font.fontname = font_model.font_name
        self.__font.generate(result_name)

    def get_font(self, result_name: str = FONT_FILE_NAME):
        """! Возвращает шрифт в бинарном представлении.
        @param result_name имя ttf-файла 
        @return  шрифт в бинарном представлении
        """

        font_file = open(self.result_name, "rb")
        data = font_file.read()
        font_file.close()
        return data