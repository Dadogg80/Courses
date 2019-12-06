# OBLIGATORISK OPPGAVE 7 UKE 8
# DELOPPGAVE 1


# oppretter en klasse Sang
class Sang:
    # konstruktør som tar imot tittel og artist
    def __init__(self, tittel, artist):
        self._tittel = tittel
        self._artist = artist

    def __str__(self):
        info = (f'Tittel: {self._tittel} | Artist: {self._artist}')
        return info

    # metode som skriver ut tittel og artisten som spilles av
    def spill(self):
        print(f'Spiller sangen {self._tittel} av {self._artist}.')

    # metode som sjekker om et eller flere av navnene i strengen navn finnes i _artist
    def sjekkArtist(self, navn):
        navnene = navn.split()
        artist = self._artist.split()
        for navn in navnene:
            if navn in artist:
                return True

    # metode som tar imot en sangtittel og sjekker om den stemmer med tittelen si sangen
    def sjekkTittel(self, tittel):
        if tittel.lower() == self._tittel.lower():
            return True

    # metode som tar imot en tittel og en artist og sjekker om det stemmer med sangen
    def sjekkArtistogTittel(self, artist, tittel):
        return (self.sjekkArtist(artist) == self.sjekkTittel(tittel))
