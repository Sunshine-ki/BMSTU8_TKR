from os.path import exists, join
from config import *
from ...FontCreation.service.fontCreator import fontCreator
from ...FontCreation.model.fontModel import fontModel


def test_font_create():
    font = fontCreator()
    font.create(fontModel())
    path_to_new_font =  join(PATH_TO_FONTCREATION, "result.ttf")
    assert exists(path_to_new_font)
