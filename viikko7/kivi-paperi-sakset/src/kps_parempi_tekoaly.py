from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu
from kps_tekoaly import KPSTekoaly

class KPSParempiTekoaly(KPSTekoaly):

    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)

    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
        tokan_siirto = self.tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {tokan_siirto}")

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = input("Ensimmäisen pelaajan siirto: ")
            tokan_siirto = self.tekoaly.anna_siirto()

            print(f"Tietokone valitsi: {tokan_siirto}")
            self.tekoaly.aseta_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)
    
    def aseta_siirto(self, ekan_siirto):
        self.tekoaly.aseta_siirto(ekan_siirto)
    
    def _toisen_siirto(self, ensimmaisen_siirto):
        return self.tekoaly.anna_siirto()

