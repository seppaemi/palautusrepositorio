from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostokset = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        if len(self.ostokset) > 0:
            n = 0
            for ostos in self.ostokset:
                n += ostos.lukumaara()
            return n
        return 0
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        if len(self.ostokset) > 0:
            n = 0
            for ostos in self.ostokset:
                n += ostos.hinta()
            return n
        return 0
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        lisaa = Ostos(lisattava)
        kori = False
        for ostos in self.ostokset:
            if ostos.tuotteen_nimi() == lisaa.tuotteen_nimi():
                ostos.muuta_lukumaaraa(1)
                kori = True
        if not kori:
            self.ostokset.append(lisaa)

    def poista_tuote(self, poistettava: Tuote):
        poista = Ostos(poistettava)
        for ostos in self.ostokset:
            if ostos.tuotteen_nimi() == poista.tuotteen_nimi():
                ostos.muuta_lukumaaraa(-1)

        filtered = list(filter(lambda x: (x.lukumaara() != 0), self.ostokset))
        self.ostokset = filtered
        # poistaa tuotteen

    def tyhjenna(self):
        self.ostokset = []
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
