import json
import configparser
import os
import telebot

import parser
import tagger
from dbhandler import Database

db = Database(data_folder='samples')

# unpack config file
config_path = os.path.join(os.path.dirname(
                           os.path.dirname(__file__)),
                           'configure/conf.ini')

config = configparser.ConfigParser()
config.read(config_path)
KEY = config['DEFAULT']['key']


# unpack string list file
replies_path = os.path.join(os.path.dirname(
                            os.path.dirname(__file__)),
                            'configure/replies.json'
                            )

with open(replies_path) as string_data:
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
    # title, singer = parser.split_title(message.audio.title)

    # bot.send_message(message.chat.id,
    #                  REPLIES['warning']['suggested_title'].format(
    #                     title
    #                     ),
    #                 parse_mode='HTML'
    #                  )
    bot.send_message(message.chat.id, "ok cool")

    file_info = bot.get_file(message.audio.file_id)
    downloaded = bot.download_file(file_info.file_path)
    db.create_folder(message.chat.id)
    db.add_file(downloaded, message.chat.id, song=True)

@bot.message_handler(content_types=['photo'])
def parse_photo(message):
    bot.send_message(message.chat.id, "cool pic")

    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded = bot.download_file(file_info.file_path)
    db.create_folder(message.chat.id)
    db.add_file(downloaded, message.chat.id, img=True)

bot.polling()
