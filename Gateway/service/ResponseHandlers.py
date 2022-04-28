"""! @brief Классы обертки для получения данных из запроса."""

import requests

from service.exceptions.GatewayExceptions import *
                       
class DetectionRespHandler:
    """! Обработчик ответа микросервиса детекции на запрос от шлюза """

    def __init__(self, config):
        """! Конструктор класса DetectionRespHandler, инициализирующий конфигурацию."""
        self.config = config

    def get_letters(self, resp):
        """! Получает глифы из ответа сервера
        @param resp ответ от сервера. 
        @throw GatewayServiceException код возврата отличен от codes.ok
        """
        if resp.status_code != requests.codes.ok:
            raise GatewayServiceException("Произошла внутрисерверная ошибка")
        return resp.json()['letters']


class RecognitionRespHandler:
    """! Обработчик ответа микросервиса нейронной сети на запрос от шлюза"""
    def __init__(self, config):
        """! Конструктор класса RecognitionRespHandler, инициализирующий конфигурацию."""
        self.config = config

    def get_recognized_letters(self, resp):
        """! Получает расапознанные глифы из ответа сервера
        @param resp ответ от сервера. 
        @throw GatewayServiceException код возврата отличен от codes.ok
        """
        if resp.status_code != requests.codes.ok:
            raise GatewayServiceException("Произошла внутрисерверная ошибка")
        
        return resp.json()['letters_recognized']


class FontCreationRespHandler:
    """! Обработчик ответа микросервиса создания шрифта на запрос от шлюза"""
    def __init__(self, config):
        """! Конструктор класса FontCreationRespHandler, инициализирующий конфигурацию."""
        self.config = config

    def get_font_file(self, resp):
        """! Получает шрифт из ответа сервера
        @param resp ответ от сервера. 
        @throw GatewayServiceException код возврата отличен от codes.ok
        """
        if resp.status_code != requests.codes.ok:
            raise GatewayServiceException("Произошла внутрисерверная ошибка")
        
        return resp 
