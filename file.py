#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding = utf8 :

import sys
import requests
import json
import time

'''
Programa que a partir de una aplicacion web sobre clima y meteorologia,
extrae los datos de la API y devuelve un prediccion del tiempo
'''


class WeatherInfo(object):
    '''clase principal para informacion meteorologica'''

    def __init__(self):
        '''constructor de la clase WeatherInfo'''
        self.forecast = self.buildMeteoData()

    def methodAlmanac(self):
        '''metodo que devuelve el historial del tiempo'''
        return self.getWeb(self.buildUrl(services["almanac"]))

    def methodHourly(self):
        '''metodo que devuelve la prevision del tiempo'''
        return self.getWeb(self.buildUrl("/hourly/q/CA/"))

    def getWeb(self, url_web):
        '''metodo que descarga la web'''
        req = requests.get(url_web)
        return self.getDictionary(req)

    def getDictionary(self, req):
        '''metodo que obtiene el diccionario a partir del xml'''
        return json.loads(req.text)

    def buildUrl(self, function):
        '''metodo que construye la url'''
        url_root = "http://api.wunderground.com/api/"
        return url_root + api_key + function + location + ".json"

    def printWeatherInfo(self):
        '''metodo que imprime la prevision del tiempo'''
        for element in self.forecast:
            print element
            print "\n"

    def buildMeteoData(self):
        '''metodo que construye la prevision del tiempo'''
        forecast = []
        almanac_info = self.extractInfoAlmanac()
        hourly_info = self.extractInfoHourly()

        current_date = time.strftime("%d-%m-%Y")
        current_time = time.strftime("%H:%M")

        forecast.append("La prevision del tiempo para el: "
                        + current_date + " a las: " + current_time + " es:")
        forecast.append(almanac_info)
        forecast.append(hourly_info)

        # calculos de la prevision de tiempo
        return forecast

    def extractInfoAlmanac(self):
        '''metodo que sirve para extraer la informacion
           del diccionario almanac'''
        info = {}
        almanac_dict = self.methodAlmanac()

        info['temp_high'] = {}
        info['temp_high']['average'] = \
            almanac_dict['almanac']['temp_high']['normal']['C']
        info['temp_high']['record'] = \
            almanac_dict['almanac']['temp_high']['record']['C']
        info['temp_high']['year'] = \
            almanac_dict['almanac']['temp_high']['recordyear']

        info['temp_low'] = {}
        info['temp_low']['average'] = \
            almanac_dict['almanac']['temp_low']['normal']['C']
        info['temp_low']['record'] = \
            almanac_dict['almanac']['temp_low']['record']['C']
        info['temp_low']['year'] = \
            almanac_dict['almanac']['temp_low']['recordyear']

        return info

    def extractInfoHourly(self):
        '''metodo que sirve para extraer la informacion
           del diccionario hourly'''
        result = []
        hourly_dict = self.methodHourly()
        hourly_dict = hourly_dict["hourly_forecast"]

        for item in hourly_dict:
            info = []
            # hour = item["FCTTIME"]["pretty"].decode("utf-8")
            info.append("la prevision para las: " + item["FCTTIME"]
                        ["pretty"].decode("utf-8") + " es:")
            # condition = item['condition']
            info.append("The weather is: " + item['condition'])
            # thermal_sensation = item['feelslike']['metric']
            info.append("The thermal condition is: " +
                        item['feelslike']['metric'])
            # snow_cover = item['snow']['metric']
            info.append("The snow cover is: " + item['snow']['metric'])
            # temp = item['temp']['metric']
            info.append("The temperature is: " + item['temp']['metric'])
            # wind_speed = item['wspd']['metric']
            info.append("The wind speed is: " + item['wspd']['metric'])
            # humidity = item['humidity']
            info.append("The humidity is: " + item['humidity'])
            # pressure = item['mslp']['metric']
            info.append("The pressure is: " + item['mslp']['metric'])
            result.append(info)

        return result


if __name__ == "__main__":
    '''programa princiapl'''

    api_key = "5020486343d0db43"
    location = None
    services = {"almanac": "/almanac/q/CA/", "hourly": "/hourly/q/CA/"}

    if api_key is None:
        api_key = sys.argv[1]
        location = sys.argv[2]
    else:
        location = sys.argv[1]

    weather_info = WeatherInfo()
    weather_info.printWeatherInfo()
