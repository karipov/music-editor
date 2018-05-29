from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TPE1, TALB

# EXAMPLE PATHS AND NAMES:
# song = 'samples/songs/Anthony Russo - California.mp3'
# image = 'samples/artworks/russo.jpg'
# artist = 'Anthony Russo'
# track = 'California'
# TODO: Make a class?

def add_artwork(song_path, image_path):
    """ Add artwork to given song path.
    """
    audio = MP3(song_path, ID3=ID3)

    audio.tags.add(
        APIC(
            encoding=3, # 3 is for utf-8
            mime='image/jpeg', # image/jpeg or image/png
            type=3, # 3 is for the cover image
            desc=u'Cover',
            data=open(image_path, 'rb').read()
            )
        )

    audio.save()

def add_artist(song_path, artist_name):
    """ Add artist name to a given song path
    """
    audio = MP3(song_path, ID3=ID3)

    audio.tags.add(
        TPE1(
            encoding=3,
            text=artist_name
            )
        )

    audio.save()

def add_name(song_path, track_name):
    pass
