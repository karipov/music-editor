import configparser
import telebot

# unpack config file
config = configparser.ConfigParser()
config.read('conf.ini')

KEY = config['DEFAULT']['KEY']
print(KEY)
