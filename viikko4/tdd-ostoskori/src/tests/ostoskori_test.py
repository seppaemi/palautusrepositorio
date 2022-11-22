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
        