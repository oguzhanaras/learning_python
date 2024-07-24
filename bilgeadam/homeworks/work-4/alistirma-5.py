def make_album(artist, album, num_songs=0):
    info = {
        'artist': artist,
        'album': album,
        'num_songs': num_songs
    }
    return info

print(make_album("john doe", "hiworld", 5))
print(make_album("jane doe", "hiworld"))
