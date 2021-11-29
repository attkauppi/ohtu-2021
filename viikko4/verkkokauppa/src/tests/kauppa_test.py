import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):

    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = self._varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = self._varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    # tehdään toteutus saldo-metodille
    def _varasto_saldo(self, tuote_id):
        if tuote_id == 1:
            return 10
        if tuote_id == 2:
            return 5
        if tuote_id == 3:
            return 0
    # tehdään toteutus hae_tuote-metodille
    def _varasto_hae_tuote(self, tuote_id):
        if tuote_id == 1:
            return Tuote(1, "maito", 5)
        if tuote_id == 2:
            return Tuote(1, "ruisleipa", 2)
        if tuote_id == 3:
            return Tuote(1, "pulla", 1)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista
    
    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikeilla parametreilla
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            ANY,
            "12345",
            self.kauppa._kaupan_tili,
            5
        )
    
    def test_kaksi_eri_ostosta_kutsuu_pankin_tilisiirtoa_oikeilla_parametreilla(self):
        """
        Aloitetaan asiointi, koriin lisätään kaksi eri tuotetta,
        joita varastossa on ja suoritetaan ostos, varmista että 
        kutsutaan pankin metodia tilisiirto oikealla asiakkaalla,
        tilinumerolla ja summalla
        """
        # Ostokset
        # self.kauppa._alusta_tuotteet()
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        # Tilisiirto oikeilla parametreilla
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            ANY,
            "12345",
            self.kauppa._kaupan_tili,
            7
        )

    def test_kaksi_samaa_ostosta_kutsuu_pankin_tilisiirtoa_oikeilla_parametreilla(self):
        """
        Aloitetaan asiointi, koriin lisätään kaksi eri tuotetta,
        joita varastossa on ja suoritetaan ostos, varmista että 
        kutsutaan pankin metodia tilisiirto oikealla asiakkaalla,
        tilinumerolla ja summalla
        """
        # Ostokset
        # self.kauppa._alusta_tuotteet()
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # Tilisiirto oikeilla parametreilla
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            ANY,
            "12345",
            self.kauppa._kaupan_tili,
            10
        )

    def test_kaksi_ostosta_joista_toinen_loppu_kutsuu_pankin_tilisiirtoa_oikeilla_parametreilla(self):
        """
        Aloitetaan asiointi, koriin lisätään kaksi eri tuotetta,
        joita varastossa on ja suoritetaan ostos, varmista että 
        kutsutaan pankin metodia tilisiirto oikealla asiakkaalla,
        tilinumerolla ja summalla
        """
        # Ostokset
        # self.kauppa._alusta_tuotteet()
        self.kauppa.aloita_asiointi()
        # Ostoskorin hinnan pitäisi vastata vain 1 kpl tuotetta 1,
        # sillä tuote 3 on loppu.
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka", "12345")

        # Tilisiirto oikeilla parametreilla
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            ANY,
            "12345",
            self.kauppa._kaupan_tili,
            5
        )
    
    def test_aloita_asiointi_nollaa_edellisen_ostoksen_tiedot(self):
        # Ostos aluksi
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # Aloitetaan asiointi uudelleen
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)

        # Maksu
        self.kauppa.tilimaksu("pekka", "12345")

        # Tilisiirto oikeilla parametreilla
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            ANY,
            "12345",
            self.kauppa._kaupan_tili,
            2
        )
    
    def test_pyydetaan_uusi_viite_jokaiseen_maksuun(self):
        # Uusi viitegeneraattori
        viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())

        # otetaan toteutukset käyttöön
        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, viitegeneraattori_mock)
        
        # Ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # Viitegeneraattoria kutsuttu kerran
        self.assertEqual(viitegeneraattori_mock.uusi.call_count, 1)

        # Uudet ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("pekka", "12345")

        # Viitegeneraattoria kutsuttu 2 kertaa
        self.assertEqual(viitegeneraattori_mock.uusi.call_count, 2)
    
    def test_kaytetaan_perakkaisten_viitekutsujen_arvoja(self):
        viitegeneraattori_mock = Mock()

        # määritellään että metodi palauttaa ensimmäisellä kutsulla 1, toisella 2 ja kolmannella 3
        viitegeneraattori_mock.uusi.side_effect = [1, 2, 3]

        kauppa = Kauppa(self.varasto_mock, self.pankki_mock, viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # Käytössä ensimmäinen viite
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            1,
            "12345",
            self.kauppa._kaupan_tili,
            5
        )

        # Toinen ostos
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # Käytössä ensimmäinen viite
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka",
            2,
            "12345",
            self.kauppa._kaupan_tili,
            5
        )












