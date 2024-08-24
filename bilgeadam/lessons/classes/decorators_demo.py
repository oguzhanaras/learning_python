standard_song = "la is la bonita"
premium_song = "crazy in love"


def premium_account(func):

    def wrapper(self, *args, **kwargs):
        if self.is_premium:
            return func(self, *args, **kwargs)
        return "premium account is required"
    return wrapper


class MusicPlayer:

    def __init__(self, username, is_premium=False):
        self.username = username
        self.is_premium = is_premium

    def play(self, song_name):
        return f"playing {song_name}"

    def open_premium(self):
        self.is_premium = True
        return self.is_premium

    @premium_account
    def access_premium(self, song_name):
        return f"playing premium song {song_name}"

    @premium_account
    def download_song(self, song_name):
        return f"downloading song {song_name}"


standard_user = MusicPlayer(username="salimunlu")
premium_user = MusicPlayer(username="ezgiemer", is_premium=True)

standard_user.access_premium(premium_song)
premium_user.access_premium(premium_song)

standard_user.open_premium()
standard_user.download_song("livin on a prayer")