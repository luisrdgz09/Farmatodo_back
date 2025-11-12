import logging
from warnings import catch_warnings

import requests

from src.farmatodo.conf.conf_url.conf_url import ConfUrl


class EndpointsEvolutions:

    def __init__(self):
        self.url = ConfUrl.get_url()

    def get_evolutions_pokemon(self,name_pokemon):
        try:
            url = f'{self.url}/{name_pokemon}'
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except Exception as e :
            logging.error(f"Error en consumir el servicio {e}")

    def get_species_pokemon(self,url):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                return "servicio no valido"
        except Exception as e :
            logging.error(f"Error en consumir el servicio {e}")




