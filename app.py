import config
import telebot
import requests
from time import sleep
import datetime

bot = telebot.TeleBot(config.token)
now = datetime.datetime.now()
types = telebot.types
logger = telebot.logger

@bot.message_handler(commands=["help"])
def greeting(message):
    bot.send_message(message.chat.id, "Привет, видимо ты всё ещё не знаком с моим списком команд \nВот он: \n/help - Возвращает список доступных команд \n/googlefornoobs - Для тех кто не умеет пользоваться гуглом \n/ytvideo - Возвращает ссылку на видео YouTube по названию")

@bot.message_handler(commands=["googlefornoobs"])
def gfn(message):
    msgCommand = message.text
    msgText = msgCommand.split(" ")
    msgParam = msgText
    msgParam.pop(0)
    msgParam = str(msgParam)
    msgParam = msgParam.replace("[","")
    msgParam = msgParam.replace("]", "")
    msgParam = msgParam.replace("'", "")
    msgParam = msgParam.replace(",", " ")
    end_url = "https://www.google.com/search?q=" + msgParam
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на страницу поиска по запросу "+msgParam, url=end_url)
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Я погуглил за тебя", reply_markup=keyboard)

@bot.message_handler(commands=["ytvideo"])
def gfn(message):
    msgCommand = message.text
    msgText = msgCommand.split(" ")
    msgParam = msgText
    msgParam.pop(0)
    msgParam = str(msgParam)
    msgParam = msgParam.replace("[","")
    msgParam = msgParam.replace("]", "")
    msgParam = msgParam.replace("'", "")
    msgParam = msgParam.replace(",", " ")
    end_url = "https://www.youtube.com/results?search_query=" + msgParam
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Посмотреть видео на YouTube по запросу "+msgParam, url=end_url)
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Я нашел видео за тебя", reply_markup=keyboard)
# @bot.message_handler(content_types=["text"])
# def default_test(message):
#     keyboard = types.InlineKeyboardMarkup()
#     url_button = types.InlineKeyboardButton(text="Перейти в Гугл", url="https://google.com/")
#     keyboard.add(url_button)
#     bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)


if __name__ == '__main__':
    bot.polling(none_stop=True)
