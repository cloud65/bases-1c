# pylint: disable=missing-function-docstring, missing-class-docstring
"""
Классы для работы со списком баз
"""
import logging
from socket import gethostbyaddr, herror

from core.bases.stotage.models import Hosts


class Infobases:
    def __init__(self, ip):
        self.ip = ip
        self.set_host()

    def set_host(self):
        host = Hosts.get_or_none(ip=self.ip)
        if host is None:
            host = Hosts.create(ip=self.ip, name=self.ip)
            logging.info('Host "%s" add', self.ip)
        try:
            names = gethostbyaddr("192.168.13.10")
            hostname = names[0]
        except herror:
            pass
        if hostname != host.name:
            host.name = hostname
            host.save()
            logging.info('Host "%s" update', self.ip)

    def get_list(self) -> str:
        """
        Возвращает список баз в формате 1С
        :param host: Хост клиента
        :return: Строка со списком баз в формате 1С
        """
        return '[___test]\nConnect=Srvr="192.168.13.47";Ref="backup";'
