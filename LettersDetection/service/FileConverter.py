"""! @brief Определение класса для конвертации файла."""
import subprocess
import os.path

class FileConverter:
    """! Класс для изменения формата файла.
    Данный класс предоставляет необходимы функционал для изменения формата файла.
    """
    def __init__(self, config):
        """! Конструктор, инициализирующий конфигурацию."""
        self.config = config

        
    def convert_png_svg(self):
        """! Конвертирует изображения из растровогог представления в веторное
        """
        png_images_count = len(os.listdir(self.config.PNG_PATH))
        for i in range(png_images_count - 1):
            number = str(i)
            if i < 10:
                number = '0' + number
            #PNG to PNM    
            subprocess.run([self.config.CONVERT_COMMAND_PATH,
                self.config.PNG_PATH + self.config.FILE_NAME + number + self.config.PNG_EXTENSION,
                 self.config.PNM_TMP])
            #PNM to SVG
            subprocess.run([self.config.POTRACE_COMMAND_PATH,
                 self.config.PNM_TMP,
                 self.config.POTRACE_KEY_SVG,
                 self.config.POTRACE_KEY_PATH,             
                 self.config.SVG_PATH + self.config.FILE_NAME + number + self.config.SVG_EXTENSION])
            subprocess.run([self.config.RM, self.config.PNM_TMP])
        
