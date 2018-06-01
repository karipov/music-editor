import json
import configparser
import telebot

import parser
import tagger
from dbhandler import Database

# TODO: DEFINE PROPERLY THE CONF AND REPLIES FILE LOCATIONS
# unpack config file
config = configparser.ConfigParser()
config.read('editor/conf.ini')
KEY = config['DEFAULT']['key']

# unpack string list
with open('editor/replies.json') as string_data:
    REPLIES = json.load(string_data)

# create bot class
bot = telebot.TeleBot(token=KEY)


# service message handlers
@bot.message_handler(commands=['start'])
def send_start(message):
    bot.send_message(message.chat.id,
                     REPLIES['service']['start']
                     )

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id,
                     REPLIES['service']['help'],
                     parse_mode='HTML'
                     )

@bot.message_handler(content_types=['audio'])
def parse_audio(message):
    title, singer = parser.split_title(messgae.audio.title)

    bot.send_message(message.chat.id,
                     REPLIES['warning']['suggested_title'].format(
                        title
                        ),
                    parse_mode='HTML'
                     )

bot.polling()
