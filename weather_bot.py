# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# from pyowm import OWM
# from pyowm.utils import config
# from pyowm.utils import timestamps

# app = ApplicationBuilder().token("919956662:AAFoLe3p4lKoJIxBx3eSeUu0mcAfEBHX3RM").build()

# async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Приветствую тебя, {update.effective_user.first_name}!')

# app.add_handler(CommandHandler("hello", hi_command))

# async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Приветствую тебя, {update.effective_user.first_name}!')

# city = input('Напришите название города: ')
# # python weather_bot.py

# owm = OWM('824743f2498c5d87628ab60a2c11c075')
# mgr = owm.weather_manager()


# observation = mgr.weather_at_place(city)
# w = observation.weather

# w.detailed_status         # 'clouds'
# w.wind()                  # {'speed': 4.6, 'deg': 330}
# w.humidity                # 87
# w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# w.rain                    # {}
# w.heat_index              # None
# w.clouds     

# temperature = w.temperature('celsius')['temp']
# print(f'В городе {city} сейчас {temperature}°C.')
# print(w.detailed_status)

# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes



# app = ApplicationBuilder().token("919956662:AAFoLe3p4lKoJIxBx3eSeUu0mcAfEBHX3RM").build()

# async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Приветствую тебя, {update.effective_user.first_name}!')


# app.add_handler(CommandHandler("hello", hi_command))
# app.add_handler(CommandHandler("hello", hi_command))
# app.add_handler(CommandHandler("hello", hi_command))



# app.run_polling()

# async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Приветствую тебя, {update.effective_user.first_name}!')

# city = input('Напришите название города: ')
# # python weather_bot.py

# owm = OWM('824743f2498c5d87628ab60a2c11c075')
# mgr = owm.weather_manager()


# observation = mgr.weather_at_place(city)
# w = observation.weather

# w.detailed_status         # 'clouds'
# w.wind()                  # {'speed': 4.6, 'deg': 330}
# w.humidity                # 87
# w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
# w.rain                    # {}
# w.heat_index              # None
# w.clouds     

# temperature = w.temperature('celsius')['temp']

# app.add_handler(CommandHandler("hello", hi_command))

import telebot
from pyowm import OWM
from pyowm.utils.config import get_default_config

bot = telebot.TeleBot("919956662:AAFoLe3p4lKoJIxBx3eSeUu0mcAfEBHX3RM")

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, 'Добро пожаловать, ' + str(message.from_user.first_name) + ',\n/start - запуск бота\n/help - команды бота\n/credits - автор бота\nЧтобы узнать погоду напишите в чат название города')

@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.chat.id, '/start - запуск бота\n/help - команды бота\n/credits - автор бота\nЧтобы узнать погоду напишите в чат название города')

@bot.message_handler(content_types=['text'])
def test(message):
	try:
		place = message.text

		config_dict = get_default_config()
		config_dict['language'] = 'ru'

		owm = OWM('824743f2498c5d87628ab60a2c11c075', config_dict)
		mgr = owm.weather_manager()
		observation = mgr.weather_at_place(place)
		w = observation.weather

		t = w.temperature("celsius")
		t1 = t['temp']
		t2 = t['feels_like']
		t3 = t['temp_max']
		t4 = t['temp_min']

		wi = w.wind()['speed']
		humi = w.humidity
		cl = w.clouds
		st = w.status
		dt = w.detailed_status
		ti = w.reference_time('iso')
		pr = w.pressure['press']
		vd = w.visibility_distance

		bot.send_message(message.chat.id, "В городе " + str(place) + " температура " + str(t1) + " °C" + "\n" + 
				"Максимальная температура " + str(t3) + " °C" +"\n" + 
				"Минимальная температура " + str(t4) + " °C" + "\n" + 
				"Ощущается как" + str(t2) + " °C" + "\n" +
				"Скорость ветра " + str(wi) + " м/с" + "\n" + 
				"Давление " + str(pr) + " мм.рт.ст" + "\n" + 
				"Влажность " + str(humi) + " %" + "\n" + 
				"Видимость " + str(vd) + "  метров" + "\n" +
				"Описание " + str(st) + "\n\n" + str(dt))

	except:
		bot.send_message(message.chat.id,"Такой город не найден!")
		print(str(message.text),"- не найден")

bot.polling(none_stop=True, interval=0)