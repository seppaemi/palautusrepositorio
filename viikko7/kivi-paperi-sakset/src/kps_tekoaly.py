from kps import KiviPaperiSakset
from tekoaly import Tekoaly

class KPSTekoaly(KiviPaperiSakset):
	def __init__(self):
		super().__init__()
		self._tekoaly = Tekoaly()

	def _toisen_siirto(self):
		siirto = self._tekoaly.anna_siirto()
		print(f"Tietokone valitsi: {siirto}")
		
		return siirto