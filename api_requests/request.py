import json

import requests

from settings.api_config import geo_key, weather_key

EXAMPLE_URL = 'https://geocode-maps.yandex.ru/1.x/?apikey=ваш API-ключ&geocode=Москва,+Тверская+улица,+дом+7'
BASE_URL = 'https://geocode-maps.yandex.ru/1.x'
BASE_URL_W = 'https://api.weather.yandex.ru/v2/forecast'


def get_city_coords(city):
    payload = {'geocode': city, 'apikey': geo_key, 'format': 'json'}
    r = requests.get(BASE_URL, params=payload)
    geo = json.loads(r.text)
    return geo['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']

def get_weather(city):
    coordinates = get_city_coords(city).split()
    payload = {'lat': coordinates[1], 'lon': coordinates[0], 'lang': 'ru_RU'}
    r = requests.get(BASE_URL_W, params=payload, headers=weather_key)
    weather_data = json.loads(r.text)
    return weather_data['fact']

#print(get_city_coords('Провидения'))
print(get_weather('Провидения'))
