
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding = utf8:

import sys
import requests
import xmltodict
# import os


class WeatherInfo(object):
    '''clase principal para informacion del tiempo'''

    def __init__(self):
        '''constructor de la clase WeatherInfo'''
        self.almanac = self.methodAlmanac()
        # self.forecast = self.methodForecast()
        # self.hourly = self.methodHourly()

    def methodForecast(self):
        '''metodo que devuelve la prevision del tiempo'''
        # info = self.getWeb(self.buildUrl("/forecast/q/CA/"))
        return self.getWeb(self.buildUrl("/forecast/q/CA/"))

    def methodAlmanac(self):
        '''metodo que devuelve el historial del tiempo'''
        info = self.getWeb(self.buildUrl("/almanac/q/CA/"))
        return info

    def methodHourly(self):
        info = self.getWeb(self.buildUrl("/almanac/q/CA/"))
        return info

    def getWeb(self, url_web):
        '''metodo que descarga la web'''
        req = requests.get(url_web)
        dic = xmltodict.parse(req.text)
        # print dic
        return dic

    def buildUrl(self, function):
        '''metodo que construye la url'''
        url_root = "http://api.wunderground.com/api/" + api_key
        return url_root + function + location + ".xml"

    def showWeatherInfo(self):
        print "esto es la prevision del tiempo"
        # almanac_dic = almanac
        # forecast_dic = self.forecast
        print self.almanac['response']['almanac']['temp_high']['normal']['C']


class Client(object):
    '''clase principal para el tiempo del cliente'''

    def __init__(self, api_key, location):
        '''constructor de la clase WeatherClient'''
        self.location = location
        self.api_key = api_key
        self.weather_info = WeatherInfo()


if __name__ == "__main__":
    '''programa princiapl'''
    api_key = sys.argv[1]
    location = sys.argv[2]
    client = Client(api_key, location)
    client.weather_info.showWeatherInfo()
