
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding = utf8:

import sys
# import requests
from bs4 import BeautifulSoup
# import xml.dom.minidom
# import xmltodic
# import json


class WeatherInfo(object):
    '''clase principal para informacion del tiempo'''

    def __init__(self):
        '''constructor de la clase WeatherInfo'''
        self.almanac = methodAlmanac()
        self.forecast = methodForecast()

    def methodForecast(self):
        pass

    def methodAlmanac(self):
        pass


class WeatherClient(object):
    '''clase principal para el tiempo del cliente'''

    def __init__(self, api_key):
        '''constructor de la clase WeatherClient'''
        self.api_key = api_key
        self.weather_info = WeatherInfo()

    def getWeb(self):
        '''metodo que descarga la web'''
        # http://api.wunderground.com/api/5020486343d0db43/almanac/q/CA/San_Francisco.json
        # http://api.wunderground.com/api/5020486343d0db43/forecast/q/CA/San_Francisco.json
        soup = BeautifulSoup(html_web, 'html.parser')
        elements = soup.find_all('div', 'dotd-title')


def buildUrl():
    pass


if __name__ == "__main__":
    '''programa princiapl'''

    api_key = None

    if api_key is None:
        try:
            api_key = sys.argv[1]
        except IndexError:
            print "La API KEY no existe"

    wc = WeatherClient(api_key)

    # construir la url final
