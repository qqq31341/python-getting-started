import collections
import sqlite3
import telebot
import logging
import requests
# import random
# import telegram
# import logging
# import aiogram
# import asyncio


from sqlighter import SQLighter
# from telebot import types
from telebot import *
from telegram.ext import *
from telegram.ext import Updater

# from telegram.ext import CallbackQueryHandler, CommandHandler
# from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = '1177956022:AAGOQLroMHsIrStZBYUU7FyZeyMRonHRPJk'
bot = telebot.TeleBot(TOKEN)
if __name__ == '__main_':
    executor.start_polling(dp, skip_updates=True)


def __init__(self, token, generator):
    self.updater = Updater(token=token)  # заводим апдейтера
    handler = MessageHandler(Filters.text | Filters.command, self.handle_message)
    self.updater.dispatcher.add_handler(handler)  # ставим обработчик всех текстовых сообщений
    self.handlers = collections.defaultdict(generator)  # заводим мапу "id чата -> генератор"
    def start(self):
        self.updater.start_polling()


@bot.message_handler(commands=['start'])
def start(message: types.Message):
    item1 = types.KeyboardButton("Розклад")
    item2 = types.KeyboardButton("Посилання на пару")
    item3 = types.KeyboardButton("Казино")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id,
                     'Привіт! Ти підписався на власного бота группи ПГ-01'.format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)
    sti = open('./welcome.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)



@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == "Розклад":
            keyboard1 = types.InlineKeyboardMarkup()
            callback_button8 = types.InlineKeyboardButton(text="Перший тиждень", callback_data="week1")
            callback_button9 = types.InlineKeyboardButton(text="Другий тиждень", callback_data="week2")
            keyboard1.add(callback_button8, callback_button9)
            bot.send_message(message.chat.id, 'Оберіть навчальний тиждень'.format(message.from_user, bot.get_me()),
                             parse_mode='html', reply_markup=keyboard1)
        elif message.text == 'Посилання на пару':
            keyboard = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="Вища Математика", callback_data="math")
            callback_button2 = types.InlineKeyboardButton(text="Програмування", callback_data="program")
            callback_button3 = types.InlineKeyboardButton(text="Іноземна мова", callback_data="lang")
            callback_button4 = types.InlineKeyboardButton(text="Матеріалознавство", callback_data="material")
            callback_button5 = types.InlineKeyboardButton(text="Інженерна графіка", callback_data="ingraph")
            callback_button6 = types.InlineKeyboardButton(text="Історія Лекція", callback_data="historylec")
            callback_button7 = types.InlineKeyboardButton(text="Історія Прак,Лаб", callback_data="historyprac")
            callback_button10 = types.InlineKeyboardButton(text="Фізика Лекції", callback_data="physlec")
            callback_button11 = types.InlineKeyboardButton(text="Фізика Прак,Лаб", callback_data="physlab")
            keyboard.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button5,
                         callback_button6, callback_button7, callback_button10, callback_button11)
            bot.send_message(message.chat.id, 'Оберіть предмет'.format(message.from_user, bot.get_me()),
                             parse_mode='html', reply_markup=keyboard)
        elif message.text == 'Казино':
             bot.send_message(message.chat.id, '🎰'.format(message.from_user, bot.get_me()),
                              parse_mode='html')

            # bot.send_message(message.chat.id, 'Оберіть предмет'.format(message.from_user, bot.get_me()),
            # parse_mode='html', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "week1":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="*Перший тиждень*", parse_mode="Markdown")
            bot.send_photo(chat_id=call.message.chat.id, photo=open('./1.png', 'rb'))
        elif call.data == "week2":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="*Другий тиждень*", parse_mode="Markdown")
            bot.send_photo(chat_id=call.message.chat.id, photo=open('./2.png', 'rb'))

        elif call.data == "program":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="*Програмування*\n \nАлексей Павловский приглашает вас на запланированную "
                                       "конференцию: Zoom.\n Тема: Програмування - 1\n Время: Это регулярная "
                                       "конференция Начать в любое время\n Подключиться к конференции Zoom\n "
                                       "https://us02web.zoom.us/j/86266278887?pwd=bFd6Z28rVk9HeWh4c1lsbG1QSVFDUT09\n "
                                       "Идентификатор конференции: 862 6627 8887\n Код доступа: 4sdZ9G",
                                  parse_mode="Markdown")

        elif call.data == "math":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Скоро будет...")

        elif call.data == "material":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="*Матеріалознавство*\n \nСергей Заец приглашает вас на запланированную "
                                       "конференцию: Zoom.\n Подключиться к конференции Zoom\n "
                                       "https://us04web.zoom.us/j/8765928915?pwd=eHhnUWFCckJHZk53UVhObmw1dlZWdz09\n "
                                       "Идентификатор конференции: 876 592 8915\n Код доступа: 6mrghS",
                                  parse_mode="Markdown")

        elif call.data == "ingraph":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="*Інженерна графіка*\n \nГалина Баскова приглашает вас на запланированную "
                                       "конференцию: Zoom.\n Тема: Вступ.Загальні правила виконання креслеників\n "
                                       "Подключиться к конференции Zoom\n "
                                       "https://us04web.zoom.us/j/3966342724?pwd=eXhKRm1Nblo0SVpJR29teEVQOFZ0QT09\n "
                                       "Идентификатор конференции: 396 634 2724\n Код доступа: cw2iGi",
                                  parse_mode="Markdown")

        elif call.data == "lang":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="*Іноземна мова*\n \nOksana Yarmolenko is inviting you to a scheduled Zoom "
                                       "meeting.\n Topic: English PG01\n Join Zoom Meeting\n "
                                       "https://us02web.zoom.us/j/83103742751?pwd=N1FzVnZPQXJZMEhDSHdMR1hUQTQzdz09\n "
                                       "Meeting ID: 831 0374 2751\n Passcode: 509826",
                                  parse_mode="Markdown")

        elif call.data == "historylec":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Скоро будет...")

        elif call.data == "historyprac":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="Скоро будет...")

        elif call.data == "physlec":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="*Історія Лекція*\n \nРамазанов Шамиль Шахович запрошує вас на конференцію\n "
                                       "https://meet.google.com/nqh-rgaj-jcq",
                                  parse_mode="Markdown")

        elif call.data == "physlab":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text="*Історія Лабораторна, Практика*\n \nПерга Юрій Миколайович запрошує вас на "
                                       "конференцію\n https://meet.google.com/vnc-jxhb-qfm",
                                  parse_mode="Markdown")


bot.polling(none_stop=True)