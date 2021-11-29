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
