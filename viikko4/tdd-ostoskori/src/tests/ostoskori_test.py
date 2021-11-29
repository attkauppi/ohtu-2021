import unittest
from ostoskori import Ostoskori
from tuote import Tuote
from ostos import Ostos

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        exp_result = 1
        self.assertEqual(exp_result, len(self.kori.ostokset()))
    
    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)

        self.assertEqual(3, self.kori.hinta())
    
        
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_on_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        leipa = Tuote("Leipä", 2)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)
        
        self.assertEqual(2, len(self.kori.ostokset()))
    
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korin_hinta_tuotteiden_hinta(self):
        maito = Tuote("Maito", 3)
        leipa = Tuote("Leipä", 2)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)

        self.assertEqual(5, self.kori.hinta())
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_2_tavaraa(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(2, len(self.kori.ostokset()))
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korin_hinta_2_kertaa_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(6, self.kori.hinta())


        