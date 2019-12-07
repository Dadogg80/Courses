from song import Song
from playlist import Playlist


def main():

    allMusikk = Playlist('Hele musikkbiblioteket')
    allMusikk.readFromFile('musikk.txt')

    print("Tester spillAlle: Spiller alle sanger i listen:")
    allMusikk.playAll()
    print()

    newSong = Song("Mil etter mil", "Jahn Teigen")
    allMusikk.addSong(newSong)
    print("Spiller alle sanger i listen inkl ny sang:")
    allMusikk.playAll()
    print()

    print("Spiller ny sang:")
    allMusikk.playSong(newSong)
    print()

    foundSong = allMusikk.findSong("Mil etter mil")
    if foundSong is not None:
        print("Fant sangen:")
        allMusikk.playSong(foundSong)
    else:
        print("Fant ikke sangen\n")
    assert(foundSong in allMusikk.getArtistSelection("Jahn"))
    print()

    # test if multiple song returns for the artist
    queenPlay = allMusikk.getArtistSelection("Queen")
    print("Spiller sanger med Queen hentet fra listen: ")
    for queenSong in queenPlay:
        queenSong.play()

    allMusikk.removeSong(foundSong)
    assert(not(foundSong in allMusikk.getArtistSelection("Jahn")))


main()
