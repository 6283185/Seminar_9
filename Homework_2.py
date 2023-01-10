# Прогноз погоды - бот

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------
city = input('Напришите название города: ')

owm = OWM('824743f2498c5d87628ab60a2c11c075')

mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place(city)
w = observation.weather

w.detailed_status         # 'clouds'
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
w.rain                    # {}
w.heat_index              # None
w.clouds     

temperature = w.temperature('celsius')['temp']
print(f'В городе {city} сейчас {temperature}°C.')
print(w.detailed_status)
