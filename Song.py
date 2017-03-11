class Song:

    def __init__(self, title, artist, year, album, filename, seconds):
        self.title = title
        self.artist = artist
        self.year = year
        self.album = album
        self.filename = filename
        self.seconds = seconds
        
    def __str__(self):
        return str(self.artist) + " - " + str(self.title)
