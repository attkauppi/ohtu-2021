class Binaarioperaatio:
    def __init__(self, sovelluslogiikka, syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.tulos = self.sovelluslogiikka.tulos
        self.syote = syote
    
    def suorita(self):
        return self.laske(self.sovelluslogiikka.hae)
    
    def laske(self, tulos):
        return 0

class Summa(Binaarioperaatio):
    def __init__(self, sovelluslogiikka, syote=0):
        super().__init__(sovelluslogiikka, syote)
    
    def laske(self, arvo):
        print("Arvo: ", arvo)
        return self.tulos + arvo

class Erotus(Binaarioperaatio):
    def __init__(self, sovelluslogiikka, syote=0):
        super().__init__(sovelluslogiikka, syote)
    
    def laske(self, arvo):
        return self.tulos - arvo

class Nollaus(Binaarioperaatio):
    def __init__(self, sovelluslogiikka, syote=0):
        super().__init__(sovelluslogiikka, syote)
    
    def laske(self, arvo):
        return 0
    
class Kumoa(Binaarioperaatio):
    def __init__(self, sovelluslogiikka, syote=0):
        super().__init__(sovelluslogiikka, syote)
    
    def laske(self, arvo):
        return 0