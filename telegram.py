import telebot
from telebot import apihelper
from Class_Href_Radius import Title_Model

nomer = '51.91.136.247'
port = '3128'

TOKEN = '971211293:AAEoornMUTnJHHxBKWGK8JVEmRpbCHbAw9g'

proxies = {
    'http': f'http://{nomer}:{port}',
    'https': f'http://{nomer}:{port}',
}

apihelper.proxy = proxies

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


# Обработка команд
@bot.message_handler(commands=['avto'])
def timer(message):
    region = ' '.join(message.text.split(' ')[1:2])
    radius = ' '.join(message.text.split(' ')[2:3])
    n = ' '.join(message.text.split(' ')[3:])
    n = int(n)
    Output_params = Title_Model(region, radius, 2)
    params = Output_params.href_models()
    for item in params[:n]:
        title = item['title']
        href = item['href']
        bot.send_message(message.chat.id,"*"*38 + title )
        bot.send_message(message.chat.id, href)

@bot.message_handler(commands=['avto_moskva_0'])
def timer(message):
    Output_params = Title_Model('moskva', 0, 2)
    params = Output_params.href_models()
    for item in params[:5]:
        title = item['title']
        href = item['href']
        bot.send_message(message.chat.id, "*" * 38 + title)
        bot.send_message(message.chat.id, href)

@bot.message_handler(commands=['avto_moskva_100'])
def timer(message):
    Output_params = Title_Model('moskva', 100, 2)
    params = Output_params.href_models()
    for item in params[:5]:
        title = item['title']
        href = item['href']
        bot.send_message(message.chat.id, "*" * 38 + title)
        bot.send_message(message.chat.id, href)

@bot.message_handler(commands=['avto_kazan_0'])
def timer(message):
    Output_params = Title_Model('kazan', 0, 2)
    params = Output_params.href_models()
    for item in params[:5]:
        title = item['title']
        href = item['href']
        bot.send_message(message.chat.id, "*" * 38 + title)
        bot.send_message(message.chat.id, href)

@bot.message_handler(commands=['avto_kazan_100'])
def timer(message):
    Output_params = Title_Model('kazan', 100, 2)
    params = Output_params.href_models()
    for item in params[:5]:
        title = item['title']
        href = item['href']
        bot.send_message(message.chat.id, "*" * 38 + title)
        bot.send_message(message.chat.id, href)


bot.polling()