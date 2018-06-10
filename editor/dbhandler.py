import sqlite3
import os

class Database():
    def __init__(self, data_folder='files'):
        self.dir = os.path.dirname(os.path.dirname(__file__))
        self.data_folder = data_folder
        self.absolute_path = os.path.join(self.dir, self.data_folder)

        # create the data folder
        if not os.path.exists(self.absolute_path):
            os.mkdir(self.absolute_path)

    def create_folder(self, user_id):
        user_path = os.path.join(self.absolute_path, str(user_id))

        if not os.path.exists(user_path):
            os.mkdir(user_path)

    def add_file(self, downloaded_file, user_id, song=False, img=False):
        if img:
            name = 'image.jpg'
        elif song:
            name = 'song.mp3'

        down_path = os.path.join(self.absolute_path, str(user_id), name)

        with open(down_path, 'wb') as file_obj:
            file_obj.write(downloaded_file)

# # test
# db = Database(data_folder='samples')
# db.create_folder(316)
