from telebot import types

# rigistry_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
# rigistry_keyboard_btn = types.KeyboardButton(text="Регистрация")
# rigistry_keyboard.add(rigistry_keyboard_btn)

rigistry_keyboard = types.InlineKeyboardMarkup(row_width=1)
rigistry_keyboard_btn = types.InlineKeyboardButton(text="Регистрация", callback_data="Registr")
rigistry_keyboard.add(rigistry_keyboard_btn)


phone_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
phone_keyboard_btn = types.KeyboardButton(text="Отправить мой номер", request_contact=True)
phone_keyboard.add(phone_keyboard_btn)


location_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
location_keyboard_btn = types.KeyboardButton(text='Отправить геопозицию', request_location=True)
location_keyboard.add(location_keyboard_btn)

remove_keyboard = types.ReplyKeyboardRemove()
