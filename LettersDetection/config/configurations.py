class Config(object):
    """! Конфигурация микросервиса детекции"""

    #All paths
    ## Путь к растровым глифам
    PNG_PATH = '../image/png/'
    ## Путь к векторным глифам
    SVG_PATH = '../image/svg/'
    ## Путь к скрипту конвертации png в svg
    PATH_TO_SCRIPT = '../script_png2svg/png2svg.sh'
    ## Путь к комманде convert
    CONVERT_COMMAND_PATH = '/usr/local/bin/convert'
    ## Путь к комманде potrace
    POTRACE_COMMAND_PATH = '/usr/local/bin/potrace'
    ## Путь к входным изображениям
    INPUT_PATH = '../image/input/' #for test version

    #Shell commands
    ## Команда для удаления
    RM = 'rm'
    ## Команда для конвертации png to pnm
    CONVERT = 'convert'
    ## Команда для конвертации pnm to svg
    POTRACE = 'potrace'

    #All extensions
    ## Путь к изображениям
    FILE_NAME = 'img'
    ## Middle file
    PNM_TMP = 'img.pnm'
    ## Растровое расширение
    PNG_EXTENSION = '.png'
    ## Веторное расширение
    SVG_EXTENSION = '.svg'

    #Potrace keys
    ## Potrace keys -s
    POTRACE_KEY_SVG = '-s'
    ## Potrace keys -o
    POTRACE_KEY_PATH = '-o'

    #Image size
    ## Размер изображения
    OUT_SIZE = 28



