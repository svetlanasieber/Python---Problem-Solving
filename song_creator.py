import os

def add_songs(*args):
    song_text = {}
    for name_song, data in args:
        if name_song not in song_text.keys():
            song_text[name_song] = []

        song_text[name_song].extend(data)
    result = []
    for song_title, song_lyrics in song_text.items():
        result.append('- ' + song_title)
        if song_lyrics:
            result.extend(song_lyrics)

    return os.linesep.join(result)