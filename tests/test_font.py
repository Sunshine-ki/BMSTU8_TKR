from os.path import exists, join

from config import *

def test_existing_base_font():
    path_to_base_font =  join(PATH_TO_FONTCREATION, "basic_font.ttf")
    assert exists(path_to_base_font)