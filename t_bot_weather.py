import telebot
from pyowm import OWM
bot = telebot.TeleBot("2042757788:AAGxW0NwH8e9JXPD1VZLPau-Wy_PZZOPzNg")
owm = OWM('ab1636337e8ac48777c9c86b81ad392d')

mgr = owm.weather_manager()

@bot.message_handler(content_types=["text"])
def send_echo(message):
	if message.text=="/start" or (message.text).lower()=="привет":
		res="Привет!\nДля какого города узнаем погоду??"
	else:
		try:
			observation = mgr.weather_at_place(message.text)
			w = observation.weather
			temp = w.temperature("celsius")["temp"]
			res = 'В городе ' + message.text + ' сейчас "' + w.detailed_status + '"'
			res += "\nТемпература сейчас всреднем "+str(temp) + "C градусов по Цельсию\n\n"
			if temp<-10:
				res += "Мороз Лютый! Шапку не забудь"
			elif temp<10:
				res += "Прохладно однако...\nПодштанники я бы натянул.."
			elif temp<20:
				res += "Жить можно, но одеться определенно стоит"
			elif temp < 25:
				res += "Прекрасная погодка для прогулки"
			elif temp > 25:
				res += "Одеваться вовсе необязательно"
		except:
			res = 'Я тебя не понял, напиши название города без ошибок!'
	bot.send_message(message.chat.id, res)
bot.polling(none_stop=True)
