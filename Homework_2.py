# Прогноз погоды - бот

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update


app = ApplicationBuilder().token("919956662:AAFoLe3p4lKoJIxBx3eSeUu0mcAfEBHX3RM").build()

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Приветствую тебя, {update.effective_user.first_name}!')


async def weather_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'В городе {city} сейчас {temperature}°C.')    


app.add_handler(CommandHandler("hello", hi_command))
# app.add_handler(CommandHandler("weather", weather))
app.add_handler(CommandHandler("weather", weather_command))

# app.add_handler(CommandHandler("hello", hi_command))
# app.add_handler(CommandHandler("hello", hi_command))
# app.add_handler(CommandHandler("hello", hi_command))




# ---------- FREE API KEY examples ---------------------
owm = OWM('824743f2498c5d87628ab60a2c11c075')
city = input('Напришите название города: ')
mgr = owm.weather_manager()


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

app.run_polling()