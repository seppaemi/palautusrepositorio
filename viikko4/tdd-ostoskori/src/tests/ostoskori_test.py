from typing import Tuple
import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
    
    def test_lisaa_yksi_tuote_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_sama_kuin_tuotteen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), maito.hinta())
    
    def test_kahden_eri_tuotteen_lisattya_korissa_2_tavaraa(self):
        maito = Tuote("Maito", 3)
        porkkana = Tuote("Porkkana", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(porkkana)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_eri_tuotteen_lisattya_korin_hinta_tuotteiden_hitnojen_summa(self):
        maito = Tuote("Maito", 3)
        porkkana = Tuote("Porkkana", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(porkkana)
        self.assertEqual(self.kori.hinta(), 8)
    
    def test_kaksi_samaa_lisattya_ostoskorissa_2_tavaraa(self):
        porkkana = Tuote("Porkkana", 5)
        self.kori.lisaa_tuote(porkkana)
        self.kori.lisaa_tuote(porkkana)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kaksi_samaa_lisattya_korin_hinta_kahdesti_tuotteen_hinta(self):
        porkkana = Tuote("Porkkana", 5)
        self.kori.lisaa_tuote(porkkana)
        self.kori.lisaa_tuote(porkkana)
        self.assertEqual(self.kori.hinta(), 10)
    
        # step 8
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset
        self.assertEqual(len(ostokset), 1)

        # testaa ett?? metodin palauttaman listan pituus 1
    
        # step 9
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset[0]
        self.assertEqual(ostos.tuote, maito)
        self.assertEqual(ostos._lukumaara, 1)

        # testaa t????ll??, ett?? palautetun listan ensimm??inen ostos on halutunkaltainen.
    
    def test_kahden_eri_tuotteen_lisayksen_jalkeen_kori_sisaltaa_kaksi_tuotetta_(self):
        maito = Tuote("Maito", 3)
        porkkana = Tuote("Porkkana", 5)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(porkkana)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskori_sisaltaa_yhden_ostoksen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostokset = self.kori.ostokset
        self.assertEqual(len(ostokset), 1)
    
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_kori_sisaltaa_sama_nimi_kuin_tuotteella_ja_lukumaara_2(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        ostos = self.kori.ostokset[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 2)

    def test_jos_korissa_kaksi_samaa_tuotetta_ja_toinen_poistetaan_jaa_koriin_tuotetta_1_kpl(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        ostos = self.kori.ostokset[0]
        self.assertEqual(ostos.lukumaara(), 1)
    
    def test_jos_koriin_on_lisatty_tuote_ja_sama_tuote_poistetaan_on_kori_tyhja(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        self.assertEqual(len(self.kori.ostokset), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)
    
    def test_metodi_tyhjenna_tyhjentaa_korin(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.tyhjenna()
        self.assertEqual(len(self.kori.ostokset), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
        self.assertEqual(self.kori.hinta(), 0)