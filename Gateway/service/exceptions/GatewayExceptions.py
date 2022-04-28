"""! @brief Класс для представления кастомной ошибки."""
import requests
            
class GatewayServiceException(Exception):
    """! Класс-представление ошибки, возможной при работе с шлюзом
    Данный класс предоставляет возможность создания кастомной ошибки.
    """
    status_code = 500
    name = "Gateway error"
    message = "Ошибка шлюза"

    def __init__(self, message, name=None, status_code=None):
        """! Конструктор класса для преобразования сохранения массива байтов в виде фотографий.
        @param message сообщение об ошибке
        """

        super().__init__()
        self.message = message
        if name is not None:
            self.name = name
        if status_code is not None:
            self.status_code = status_code
