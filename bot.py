import telebot
import requests

bot = telebot.TeleBot('695717859:AAFSt8hkwJMOQuFFnRC6Po_SJa5hmnhJLqQ', threaded=False)


@bot.message_handler(content_types=['text'])
def translate(message):
    text = message.text
    token = 'trnsl.1.1.20181010T214428Z.ceda94436df92606.b37884e3e65b36d66e9354aaaa0f1b0d12908b9f'
    url_trans = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    trans_option = {'key': token, 'lang': 'ru-en', 'text': text}
    webRequest = requests.get(url_trans, params=trans_option)
    translated = webRequest.text[36:-3]
    bot.send_message(chat_id=message.chat.id, text=translated)


bot.polling(none_stop=True)
