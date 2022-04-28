"""! @brief Определение метаданных шрифта."""
##
# @file fontCreator.py
#
# Copyright (c) 2020 Sunshine-ki.

class fontModel:
    """! Класс описывающий метаданные шрифта.
    Данный класс предоставляет метаданные шрифта.
    """

    font_name: str 

    def __init__(self):
        ## Название шрифта
        self.font_name = "own"