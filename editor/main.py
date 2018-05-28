import json
import configparser
import telebot

# TODO: DEFINE PROPERLY THE CONF AND REPLIES FILE LOCATIONS
# unpack config file
config = configparser.ConfigParser()
config.read('editor/conf.ini')
KEY = config['DEFAULT']['key']

# unpack string list
with open('editor/replies.json') as string_data:
    replies = json.load(string_data)

# create bot class
bot = telebot.TeleBot(token=KEY)


# service message handlers
@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id,
                     replies['service_replies']['start'])

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id,
                     replies['service_replies']['help'],
                     parse_mode='HTML')

bot.polling()
