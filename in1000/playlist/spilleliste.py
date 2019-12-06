from sang import Sang


class Spilleliste:
    def __init__(self, listenavn):
        self._sanger = []
        self._navn = listenavn

    # metoden åpner en fil og leser innholdet
    def lesFraFil(self, filnavn):
        with open(filnavn, 'r') as fil:
            # for hver linje i filen
            for linje in fil:
                # split() linjen ved ';'
                alleData = linje.strip().split(';')
                nySang = Sang(alleData[0], alleData[1])
                self.leggTilSang(nySang)

    # metoden legger til nySang fra fil til spillelisten
    def leggTilSang(self, nySang):
        self._sanger.append(nySang)

    # metoden tar mot en sang og fjerner den sangen fra spillelisten
    def fjernSang(self, sang):
        if sang in self._sanger:
            self._sanger.pop()

    # metoden spiller av sangen
    def spillSang(self, sang):
        sang.spill()

    # metoden spiller av alle sangene i spillelisten
    def spillAlle(self):
        for enSang in self._sanger:
            self.spillSang(enSang)

    # metoden tar imot en sangtittel og undersøker om denne finnes i spillelisten
    def finnSang(self, tittel):
        for enSang in self._sanger:
            sjekk = enSang.sjekkTittel(tittel)
            if sjekk:
                return enSang

    def hentArtistUtvalg(self, artistNavn):
        listen = []
        for enArtist in self._sanger:
            sjekk = enArtist.sjekkArtist(artistNavn)
            if sjekk:
                listen.append(enArtist)
        return listen
