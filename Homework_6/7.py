"""
Переделать программу с погодой так что бы она 
запрашивала город а в ответ выдавала подробную информацию 
о погоде в этом городе в красивом формате.
"""

# pip install pyowm
# pip install --upgrade setuptools

from pyowm import OWM
from pprint import pprint

owm = OWM('3b7520cfa14d8220f49bed37a19a7b4d')
mgr = owm.weather_manager()

city = input("Enter a city name: ")

# Получение данных
observation = mgr.weather_at_place(city)
weather = observation.weather

# Сохраняем данные в словарь
weather_data = {
    "City": city.title(),
    "Status": weather.detailed_status,
    "Temperature (°C)": weather.temperature('celsius'),
    "Humidity (%)": weather.humidity,
    "Pressure (hPa)": weather.pressure['press'],
    "Wind (m/s)": weather.wind()['speed']
}

print("\n📋 Weather Information:")
pprint(weather_data, sort_dicts=False)


# Или c помощью tabulate

# pip install tabulate

from tabulate import tabulate

# Собираем данные
temp = weather.temperature('celsius')

table = [
    ["City", city.title()],
    ["Status", weather.detailed_status],
    ["Temp (°C)", temp['temp']],
    ["Temp min (°C)", temp['temp_min']],
    ["Temp max (°C)", temp['temp_max']],
    ["Humidity (%)", weather.humidity],
    ["Pressure (hPa)", weather.pressure['press']],
    ["Wind (m/s)", weather.wind()['speed']],
]

# Выводим таблицу
print("\n📊 Weather Info:")
print(tabulate(table, headers=["Parameter", "Value"], tablefmt="fancy_grid"))