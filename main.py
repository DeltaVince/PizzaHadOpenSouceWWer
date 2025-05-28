import telebot
from telebot import types


pizza_component_join = []
feature = 0
calories = 0
products = {
    "лук",
    "сыр",
    "колбаса",
    "салат", 
    "ананасы",
    "грибы"
}

bot = telebot.TeleBot("7650812272:AAEOtwEnb93SRhuK_JMFJqLqthFqsOXKv-w")

@bot.message_handler(commands=["start"])
def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    web_app_button = types.KeyboardButton(
        "Перейти к Созданию пиццы",
        web_app=types.WebAppInfo(
            url="https://pizza-had-open-souce-w-wer.vercel.app/"  
        ),
    )
    markup.add(web_app_button)

    bot.send_message(
        message.chat.id,
        "Конструктор Пицц!",
        reply_markup=markup,
    )


if __name__ == "__main__":
    bot.polling(none_stop=True)
