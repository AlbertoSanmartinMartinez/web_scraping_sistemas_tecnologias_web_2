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

    def methodAlmanac(self):
        '''metodo que devuelve el historial del tiempo'''
        return self.getWeb(self.buildUrl(services["almanac"]))

    def methodHourly(self):
        '''metodo que devuelve la prevision del tiempo'''
        return self.getWeb(self.buildUrl(services["hourly"]))

    def getWeb(self, url_web):
        '''metodo que descarga la web'''
        req = requests.get(url_web)
        return self.getDictionary(req)

    def getDictionary(self, req):
        '''metodo que obtiene el diccionario a partir del json'''
        return json.loads(req.text)

    def buildUrl(self, function):
        '''metodo que construye la url'''
        url_root = "http://api.wunderground.com/api/"
        return url_root + api_key + function + location + ".json"

    def buildMeteoData(self):
        '''metodo que construye la prevision del tiempo'''
        almanac_info = self.extractInfoAlmanac()
        hourly_info = self.extractInfoHourly()

        current_date = time.strftime("%d-%m-%Y")
        print "Weather info for " + current_date + " in " + location.title()

        tips = []

        self.printTips(tips)
        self.printHourly(hourly_info)
        self.printAlmanac(almanac_info)

    def extractInfoAlmanac(self):
        '''metodo que sirve para extraer la informacion
           del diccionario almanac'''
        l = []
        almanac_dict = self.methodAlmanac()
        aux = almanac_dict['almanac']['temp_high']['normal']['C']
        l.append("Aaverage maximum temperature: " + aux + "ºC".decode("utf-8"))
        aux = almanac_dict['almanac']['temp_high']['record']['C']
        l.append("Maximum temperature record: " + aux + "ºC".decode("utf-8"))
        aux = almanac_dict['almanac']['temp_high']['recordyear']
        l.append("Record year: " + aux)
        aux = almanac_dict['almanac']['temp_low']['normal']['C']
        l.append("Average minimum temperature: " + aux + "ºC".decode("utf-8"))
        aux = almanac_dict['almanac']['temp_low']['record']['C']
        l.append("Minimum temperaturerecord: " + aux + "ºC".decode("utf-8"))
        aux = almanac_dict['almanac']['temp_low']['recordyear']
        l.append("Record year: " + aux)

        return l

    def extractInfoHourly(self):
        '''metodo que sirve para extraer la informacion
           del diccionario hourly'''
        l = []
        hourly_dict = self.methodHourly()
        hourly_dict = hourly_dict["hourly_forecast"]

        for item in hourly_dict:
            info = []
            info.append("Weather information for " + item["FCTTIME"]
                        ["pretty"] + " :")

            print item["FCTTIME"]["pretty"]

            info.append("Condition: " + item['condition'])
            info.append("Thermal condition: " +
                        item['feelslike']['metric'])
            info.append("Snow cover: " + item['snow']['metric'])
            info.append("Temperature: " + item['temp']['metric'])
            info.append("Wind speed: " + item['wspd']['metric'])
            info.append("Humidity: " + item['humidity'])
            info.append("Pressure: " + item['mslp']['metric'])
            l.append(info)

        return l

    def printAlmanac(self, almanac_info):
        print "Historical weather information:"
        for item in almanac_info:
            print item

    def printHourly(self, hourly_info):
        for item in hourly_info:
            print item
            for element in item:
                print element
            print "\n"

    def printTips(self, tips):
        for item in tips:
            print item


if __name__ == "__main__":
    '''programa princiapl'''

    api_key = "5020486343d0db43"
    location = "Lleida"
    services = {"almanac": "/almanac/q/CA/", "hourly": "/hourly/q/CA/"}

    if api_key is None:
        api_key = sys.argv[1]

    weather_info = WeatherInfo()
    weather_info.buildMeteoData()
