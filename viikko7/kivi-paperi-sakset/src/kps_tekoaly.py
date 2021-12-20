from tuomari import Tuomari
from tekoaly import Tekoaly
from kps import KPS

class KPSTekoaly(KPS):

    def __init__(self):
        self.tekoaly = Tekoaly()

    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        print(f"Tietokone valitsi: {tokan_siirto}")

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = self._toisen_siirto(ekan_siirto)

            print(f"Tietokone valitsi: {tokan_siirto}")

        print("Kiitos!")
        print(tuomari)
    
    def _toisen_siirto(self, ensimmaisen_siirto):
        return self.tekoaly.anna_siirto()

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
