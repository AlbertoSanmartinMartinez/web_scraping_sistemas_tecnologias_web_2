
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding = utf8:

import sys
import requests
import xmltodict

'''
Programa que a partir de una aplicacion web sobre clima y meteorologia
hace web scraping de los datos y devuelve un prediccion al usuario
'''


class Client(object):
    '''clase principal para los datos del cliente'''

    def __init__(self, api_key, location):
        api_key = api_key
        location = location
        self.weather_info = WeatherInfo()

    def showWeatherInfo(self):
        print self.weather_info


class WeatherInfo(object):
    '''clase principal para informacion meteorologica'''

    def __init__(self):
        '''constructor de la clase WeatherInfo'''
        ownForecast = calculateOwnForecast()

        almanac_dict = methodAlmanac()
        hourly_dict = methodHourly()
        meteorologicaldata = MeteorologicalData(almanac_dict, hourly_dict)
        text = []

    def methodAlmanac(self):
        '''metodo que devuelve el historial del tiempo'''
        return self.getWeb(self.buildUrl("/almanac/q/CA/"))

    def methodHourly(self):
        return self.getWeb(self.buildUrl("/almanac/q/CA/"))

    def getWeb(self, url_web):
        '''metodo que descarga la web'''
        req = requests.get(url_web)
        return self.getDictionary(req)

    def getDictionary(self, req):
        '''metodo que obtiene el diccionario a partir del xml'''
        return xmltodict.parse(req.text)

    def buildUrl(self, function):
        '''metodo que construye la url'''
        url_root = "http://api.wunderground.com/api/"
        return url_root + Client.api_key + function + Client.location + ".xml"

    def showWeatherInfo(self):
        print self.meteorologicaldata
        print self.text

    def calculateOwnForecast(self):
        '''metodo que calcula la informacion para la prevision
        a partir de los diccionarios obtenidos'''
        information = []
        # tabla para las horas
        almanac_dict = self.methodAlmanac()
        hourly_dict = self.methodHourly()

        md = MeteorologicalData(almanac_dict, hourly_dict)
        return md
        # return information


class MeteorologicalData (object):
    '''clase principal para los datos del clima'''

    def __init__(self, almanac_dict, hourly_dict):
        current_time = time.strftime("%Y-%m-%d %H:%M")
        # weather_condition = hourly_dict[]
        # thermal_sensation
        # snow_cover
        # mean_sea_level_pressure
        # max_temperature =
        # min_temperatura =


if __name__ == "__main__":
    '''programa princiapl'''

    api_key = "5020486343d0db43"
    location = None

    if api_key is None:
        api_key = sys.argv[1]
        location = sys.argv[2]
    else:
        location = sys.argv[1]

    client = Client(api_key, location)
