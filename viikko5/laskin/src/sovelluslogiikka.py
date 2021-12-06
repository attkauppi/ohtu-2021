class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
    
    def hae_tulos(self):
        return self.tulos

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo
