class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen = tulos

    def miinus(self, arvo):
        self. edellinen = self.tulos
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self. edellinen = self.tulos
        self.tulos = self.tulos + arvo

    def nollaa(self, arvo):
        self. edellinen = self.tulos
        self.tulos = arvo

    def aseta_arvo(self, arvo):
        self.tulos = self.edellinen
        self.edellinen = arvo