# Week 8 - Obligatorical Assignment 7, Part 1


# Make a class Song with constructor that takes attributes title and artist
class Song:
    def __init__(self, title, artist):
        self._title = title
        self._artist = artist

    def __str__(self):
        string = (f'Title: {self._title} | Artist: {self._artist}')
        return string

    # Method that plays the song (in this assaignmet the method only prints a string to the terminal)
    def play(self):
        print(f'Playing {self._title} by {self._artist}.')

    # Method that checks if one or more of the artist names is present in the variable self._artist
    def checkArtist(self, name):
        names = name.split()
        artist = self._artist.split()
        for name in names:
            if name in artist:
                return True

    # Method recieves a title attribute and checks it with self._title
    def checkTitle(self, title):
        if title.lower() == self._title.lower():
            return True

    # Method recieves the attributes artist and title, then checks it with check methods
    def checkArtistAndTitle(self, artist, title):
        return (self.checkArtist(artist) == self.checkTitle(title))
