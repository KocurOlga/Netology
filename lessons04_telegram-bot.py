import telebot as tb

token = '1885769929:AAFgScXRhPRDTxETcTbwJSDH37e0mx_FlfM' 

bot = tb.TeleBot(token) #инициализация бота по токену

#прописываем, что бот должен делать
#функция "эхо"
@bot.message_handler(content_types=['text']) #регистрируем функцию echo в боте
def echo(message):
    bot.send_message(message.chat.id, message.text) #отправляет в чат, в котором идет сообшение тот же текст, который пришел

bot.polling(none_stop=True) #метод polling позволяет получать сообщения, "режим ожидания" сообщений
