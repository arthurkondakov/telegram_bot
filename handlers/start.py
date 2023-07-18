from config import bot
from keyboard.start import rigistry_keyboard, phone_keyboard, location_keyboard, remove_keyboard
from config import db, cursor
from db.main_db_scripts import enter_user_info





def send_messages(message):
    cursor.execute(f"""SELECT user_id FROM 'users'
                      WHERE user_id = {message.from_user.id}
                    """)
    check_user = cursor.fetchone()
    print(check_user)
    if check_user is None:
        enter_user_info(message.from_user.id, message.from_user.first_name, message.from_user.last_name,
                    message.from_user.username, message.date)
    bot.delete_message(chat_id=message.chat.id, message_id=message.id)
    with open("./images/images.jpeg", 'rb') as file:
        bot.send_photo(message.chat.id, file, caption=f"Привет! @{message.from_user.username} \n"
                                                        f"Твоё имя {message.from_user.first_name}",
                       reply_markup=rigistry_keyboard)
    # bot.send_message(message.chat.id, f"Привет! @{message.from_user.username} \n"
    #                                   f"Твоё имя {message.from_user.first_name}",
    #                  reply_markup=rigistry_keyboard)


# def request_name_user(message):
#     name = bot.send_message(message.chat.id, "Введите имя:")
#     bot.register_next_step_handler(name, request_age_user)
def request_name_user(callback):
    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.id)
    name = bot.send_message(callback.message.chat.id, "Введите имя:")
    print(name)
    bot.register_next_step_handler(name, request_age_user, name.message_id)


def request_age_user(message, name_message_id):

    bot.delete_message(chat_id=message.chat.id, message_id=name_message_id)
    bot.delete_message(chat_id=message.chat.id, message_id=message.id)
    name = message.text
    cursor.execute(f"""INSERT INTO 'form_info' (
                   user_id,
                    user_name) VALUES (
                   {message.from_user.id},
                   '{name}')
                """)
    db.commit()
    age = bot.send_message(message.chat.id, "Введите свой возраст:")
    bot.register_next_step_handler(age, request_phone_user)


def request_phone_user(message):
    age = message.text
    cursor.execute(f"""UPDATE 'form_info' SET
                       age_user = {age} WHERE user_id = {message.from_user.id}
                    """)
    db.commit()
    phone = bot.send_message(message.chat.id, "Введите номер телефона:", reply_markup=phone_keyboard)
    bot.register_next_step_handler(phone, request_city_user)


def request_city_user(message):
    phone = 0
    if message.contact:
        phone = message.contact.phone_number
        cursor.execute(f"""UPDATE 'form_info' SET
                               phone_user = {phone} WHERE user_id = {message.from_user.id}
                            """)
        db.commit()
    elif message.text:
        phone = message.text
        cursor.execute(f"""UPDATE 'form_info' SET
                                       phone_user = {phone} WHERE user_id = {message.from_user.id}
                                    """)
        db.commit()
    city = bot.send_message(message.chat.id, "Введите свой город:", reply_markup=location_keyboard)
    bot.register_next_step_handler(city, send_info)


def send_info(message):
    cursor.execute(f"""SELECT * FROM 'form_info'
                      WHERE user_id = {message.from_user.id}
                    """)
    last_users = cursor.fetchall()[-1]
    bot.send_message(message.chat.id, f"Твоё имя: {last_users[1]} \n"
                                      f"Твой возраст: {last_users[2]} \n"
                                      f"Твой номер телефона: {last_users[3]} \n", reply_markup=remove_keyboard)
    # bot.send_location(message.chat.id, latitude=message.location.latitude, longitude=message.location.longitude)



def start_message_handler():
    bot.register_message_handler(send_messages, commands=["start"])
    # bot.register_message_handler(request_name_user, func=lambda message: message.text == "Регистрация")
    bot.register_callback_query_handler(request_name_user, func=lambda callback: callback.data == "Registr")




