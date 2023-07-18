import telebot
import sqlite3

bot = telebot.TeleBot("id_bot")

db = sqlite3.connect('db.db', check_same_thread=False)
cursor = db.cursor()