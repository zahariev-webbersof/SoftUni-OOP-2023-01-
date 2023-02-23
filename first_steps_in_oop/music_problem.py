class Music:
    def __init__(self, title: str, artist: str, lyrics: str):
        self.title = title
        self.artist = artist
        self.lyrics = lyrics

    def play(self):
        return self.lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'


song = Music("Title", "Artist", "Lyrics")
print(song.print_info())
print(song.play())
