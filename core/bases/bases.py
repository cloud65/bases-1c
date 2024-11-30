# pylint: disable=missing-function-docstring, missing-class-docstring
"""
Классы для работы со списком баз
"""
class Infobases:
    def get_list(self, host:str)->str:
        """
        Возвращает список баз в формате 1С
        :param host: Хост клиента
        :return: Строка со списком баз в формате 1С
        """
        return '[___test]\nConnect=Srvr="192.168.13.47";Ref="backup";'
