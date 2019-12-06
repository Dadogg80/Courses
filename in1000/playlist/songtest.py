from song import Song


def main():
    song1 = Song("Shallow", "Lady Gaga and Bradley Cooper")
    print("Spiller av test-objekt:")
    song1.play()

    print("Tester sjekkArtist med 'Lady Gaga and Bradley Cooper'")
    assert(song1.checkArtist("Lady Gaga and Bradley Cooper"))     # True
    print("Tester sjekkArtist med 'Lord Gaga'")
    assert(song1.checkArtist("Lord Gaga"))        # True, ett ord finnes i artistnavnet
    print("Tester sjekkArtist med 'Sadley'")
    assert(not song1.checkArtist("Sadley"))       # False
    print()

    print("Tester sjekkTittel med 'Shallow'")
    assert(song1.checkTitle("Shallow"))          # True
    print("Tester sjekkTittel med 'shalLow'")
    assert(song1.checkTitle("shalLow"))          # True
    print("Tester sjekkTittel med 'Hallow'")
    assert(not song1.checkTitle("Hallow"))       # False
    print()

    print("Utforer spill:")
    song1.play()
    print()

    print("Tester sjekkArtistogTittel med 'Bradley Cooper' og 'Shallow'")
    assert(song1.checkArtistAndTitle('Bradley Cooper', 'Shallow'))  # True
    print("Tester sjekkArtistogTittel med 'Booper' og 'Shallow'")
    assert(not song1.checkArtistAndTitle('Booper', 'Shallow'))  # False

    print('Tester __str__ metode for objektet sang')
    print(song1)


main()
