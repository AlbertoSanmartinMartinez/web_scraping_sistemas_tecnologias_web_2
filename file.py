
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding = utf8:

import sys
# import requests
# from bs4 import BeautifulSoup
# import xml.dom.minidom
import xmltodict
# import json


class Client(object):
    '''clase principal para el tiempo del cliente'''

    def __init__(self, api_key, location):
        '''constructor de la clase WeatherClient'''
        self.location = location
        self.api_key = api_key
        self.weather_info = Client.WeatherInfo()

    def showWeatherInfo():
        pass

    class WeatherInfo(object):
        '''clase principal para informacion del tiempo'''

        def __init__(self):
            '''constructor de la clase WeatherInfo'''
            self.almanac = self.methodAlmanac()
            self.forecast = self.methodForecast()

        def methodForecast(self):
            '''metodo que devuelve la prevision del tiempo'''
            info = self.getWeb(self.buildUrl("/forecast/q/CA/"))
            return info

        def methodAlmanac(self):
            '''metodo que devuelve el historial del tiempo'''
            info = self.getWeb(self.buildUrl("/almanac/q/CA/"))
            return info

        def getWeb(self, url_web):
            '''metodo que descarga la web'''
            # http://api.wunderground.com/api/5020486343d0db43/forecast/q/CA/San_Francisco.json
            document_file = open(url_web, "r")
            original_doc = document_file.read()
            document = xmltodict.parse(original_doc)
            return document

        def buildUrl(self, function):
            '''metodo que construye la url'''
            url_root = "http://api.wunderground.com/api/"
            api_key
            url_final = url_root + api_key + function + Client.location + ".xml"
            return url_final


if __name__ == "__main__":
    '''programa princiapl'''

    api_key = None
    location = None

    if api_key is None or location is None:
        try:
            api_key = sys.argv[1]
            location = sys.argv[2]
        except IndexError:
            print "La API KEY o la localizacion no existe"

    client = Client(api_key, location)
    client.showWeatherInfo()
