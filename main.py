from config import bot
from handlers.start import start_message_handler
from db.create_tables import create_tables

start_message_handler()
create_tables()
# @bot.message_handler(commands=["start", "restart"])
# def send_messages(message):
#     bot.send_message(message.chat.id, f"Привет! @{message.from_user.username} \n"
#                                       f"Твоё имя {message.from_user.first_name}")

#
# @bot.message_handler(func=lambda message:"реклама" in message.text)
# def send_answer(message):
#     bot.send_message(message.chat.id, text="Получи подарок")
#
#
# @bot.message_handler(content_types=["text"])
# def replay_text(message):
#     bot.send_message(message.chat.id, text=message.text)














bot.infinity_polling()




