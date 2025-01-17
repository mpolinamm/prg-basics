class Song:
    def __init__(self, artist, title, album, year):
        self.artist = artist
        self.title = title
        self.album = album
        self.year = year

    def __str__(self):
        return (f"Performer: {self.artist}\n"
                f"Title:     {self.title}\n"
                f"Album:     {self.album}\n"
                f"Year:      {self.year}")

song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
song2 = Song("Queen", "Bohemian Rhapsody", "A Night at the Opera", 1975)

print(song1)
print()  
print(song2)
