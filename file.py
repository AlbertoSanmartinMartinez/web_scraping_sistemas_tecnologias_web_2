
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding = utf8:

import sys
import requests
import json

'''
Programa que a partir de una aplicacion web sobre clima y meteorologia,
extrae los datos de la API y devuelve un prediccion del tiempo
'''


class WeatherInfo(object):
    '''clase principal para informacion meteorologica'''

    def __init__(self):
        '''constructor de la clase WeatherInfo'''
        self.almanac_dict = self.methodAlmanac()
        self.hourly_dict = self.methodHourly()
        self.forecast = self.buildMeteoData()

    """
    def printMeteoData(self):
        pass
    """

    def methodAlmanac(self):
        '''metodo que devuelve el historial del tiempo'''
        return self.getWeb(self.buildUrl("/almanac/q/CA/"))

    def methodHourly(self):
        return self.getWeb(self.buildUrl("/hourly/q/CA/"))

    def getWeb(self, url_web):
        '''metodo que descarga la web'''
        req = requests.get(url_web)
        return self.getDictionary(req)

    def getDictionary(self, req):
        '''metodo que obtiene el diccionario a partir del xml'''
        return json.dumps(req.json())  # req.json()  json.load(req)

    def buildUrl(self, function):
        '''metodo que construye la url'''
        url_root = "http://api.wunderground.com/api/"
        return url_root + api_key + function + location + ".json"

    def printWeatherInfo(self):
        print self.forecast

    def buildMeteoData(self):
        pass
        # alamac_info = self.extractInfoAlmanac()
        # hourly_info = self.extractInfoHourly()

        # current_time = time.strftime("%Y-%m-%d %H:%M")
        # hour_forecast =
        # weather_condition =
        # thermal_sensation =
        # snow_cover
        # mean_sea_level_pressure
        # max_temperature =
        # min_temperatura =

        # return forecast

    def extractInfoAlmanac(self):
        pass

    def extractInfoHourly(self):
        pass


if __name__ == "__main__":
    '''programa princiapl'''

    api_key = "5020486343d0db43"
    location = None

    if api_key is None:
        api_key = sys.argv[1]
        location = sys.argv[2]
    else:
        location = sys.argv[1]

    weather_info = WeatherInfo()
    # weather_info.printWeatherInfo()
