from tuote import Tuote
from ostos import Ostos
import logging
class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.ostokset_lista = []

    def tavaroita_korissa(self):
        return 0
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinta = 0
        for i in self.ostokset():
            hinta += i.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        ostos = Ostos(lisattava)

        tuote_korissa = self.hae_ostoksista(ostos)
        if tuote_korissa is not None:
            ostos_korissa = self.ostokset_lista[tuote_korissa]
            ostos_korissa.muuta_lukumaaraa(1)
            self.ostokset_lista[tuote_korissa] = ostos_korissa
        else:
            self.ostokset_lista.append(ostos)
    
    def valitse_ensimmainen(self, iterable, default=None):
        for item in iterable:
            return item
        return default

    def hae_ostoksista(self, tuote):

        for count, ele in enumerate(self.ostokset()):
            if ele.tuotteen_nimi() == tuote.tuotteen_nimi():
                return count
        return None

    def poista_tuote(self, poistettava: Tuote):
        tuote_korissa = self.hae_ostoksista(poistettava)
        if tuote_korissa is not None:
            ostos = self.ostokset()[tuote_korissa]

            if ostos.lukumaara() > 1:
                ostos.muuta_lukumaaraa(-1)
                self.ostokset_lista[tuote_korissa] = ostos

            else:
                del self.ostokset_lista[tuote_korissa]

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.ostokset_lista
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
