from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Standard:
	"""Standard commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("standard", core, parent)

	def set(self, standard: float) -> None:
		"""SCPI: CONFigure:STANdard \n
		Snippet: driver.applications.k91Wlan.configure.standard.set(standard = 1.0) \n
		This remote control command specifies which WLAN standard the option is configured to measure. The availability of many
		commands depends on the selected standard! \n
			:param standard: 0 IEEE 802.11a 1 IEEE 802.11b 2 IEEE 802.11j (10 MHz) 3 IEEE 802.11j (20 MHz) 4 IEEE 802.11g To distinguish between OFDM and DSSS use the command [SENSe:]DEMod:FORMat:BANalyze:BTYPe. By default, the R&S FSW WLAN application selects the most recently defined PPDU type. 6 IEEE 802.11n 7 IEEE 802.11n (MIMO) 8 IEEE 802.11ac 9 IEEE 802.11p 10 IEEE 802.11ax 11 IEEE 802.11be
		"""
		param = Conversions.decimal_value_to_str(standard)
		self._core.io.write(f'CONFigure:STANdard {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:STANdard \n
		Snippet: value: float = driver.applications.k91Wlan.configure.standard.get() \n
		This remote control command specifies which WLAN standard the option is configured to measure. The availability of many
		commands depends on the selected standard! \n
			:return: standard: 0 IEEE 802.11a 1 IEEE 802.11b 2 IEEE 802.11j (10 MHz) 3 IEEE 802.11j (20 MHz) 4 IEEE 802.11g To distinguish between OFDM and DSSS use the command [SENSe:]DEMod:FORMat:BANalyze:BTYPe. By default, the R&S FSW WLAN application selects the most recently defined PPDU type. 6 IEEE 802.11n 7 IEEE 802.11n (MIMO) 8 IEEE 802.11ac 9 IEEE 802.11p 10 IEEE 802.11ax 11 IEEE 802.11be"""
		response = self._core.io.query_str(f'CONFigure:STANdard?')
		return Conversions.str_to_float(response)
