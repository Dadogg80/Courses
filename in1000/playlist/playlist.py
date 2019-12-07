from song import Song


class Playlist:
    def __init__(self, playlistName):
        self._songs = []
        self._name = playlistName

    # Method opens a file and reads the content
    def readFromFile(self, fileName):
        with open(fileName, 'r') as file:
            # for each line in file
            for line in file:
                # split the line at ';'
                bits = line.strip().split(';')
                # add song to playlist
                self.addSong(Song(bits[0], bits[1]))

    # Method adds the newSong to the playlist
    def addSong(self, newSong):
        self._songs.append(newSong)

    # Method removes the song from the playlist
    def removeSong(self, song):
        if song in self._songs:
            self._songs.pop()

    # Method plays the song
    def playSong(self, song):
        song.play()

    # Method plays all the songs in the playlist one by one
    def playAll(self):
        for oneSong in self._songs:
            self.playSong(oneSong)

    # Method searches for a song in the playlist
    def findSong(self, title):
        for oneSong in self._songs:
            if oneSong.checkTitle(title):
                return oneSong

    # Methods serches for an artist and makes a new playlist of the search results
    def getArtistSelection(self, artistName):
        newPlaylist = []
        for oneArtist in self._songs:
            check = oneArtist.checkArtist(artistName)
            if check:
                newPlaylist.append(oneArtist)
        return newPlaylist
