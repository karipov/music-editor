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

    def add_song_file():
        pass

    def add_album_file():
        pass

# # test
# db = Database(data_folder='samples')
# db.create_folder(316)
