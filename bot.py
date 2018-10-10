import telebot
from googletrans import Translator

bot = telebot.TeleBot('695717859:AAFSt8hkwJMOQuFFnRC6Po_SJa5hmnhJLqQ', threaded=False)


@bot.message_handler(content_types=['text'])
def translate(message):
    tr = Translator()
    translated = tr.translate(message.text, dest='en').text
    bot.send_message(chat_id=message.chat.id, text=translated)


bot.polling(none_stop=True)
