from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, num_data_symbols: float) -> None:
		"""SCPI: [SENSe]:DEMod:FORMat:BANalyze:SYMBols:OFFSet \n
		Snippet: driver.applications.k91Wlan.sense.demod.formatPy.banalyze.symbols.offset.set(num_data_symbols = 1.0) \n
		For IEEE 802.11a, ac, g (OFDM) , j, n, p signals only: This command specifies the number of data symbols from the start
		of each PPDU that are to be skipped before symbols take part in analysis. \n
			:param num_data_symbols: integer Range: 0 to 10000
		"""
		param = Conversions.decimal_value_to_str(num_data_symbols)
		self._core.io.write(f'SENSe:DEMod:FORMat:BANalyze:SYMBols:OFFSet {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:DEMod:FORMat:BANalyze:SYMBols:OFFSet \n
		Snippet: value: float = driver.applications.k91Wlan.sense.demod.formatPy.banalyze.symbols.offset.get() \n
		For IEEE 802.11a, ac, g (OFDM) , j, n, p signals only: This command specifies the number of data symbols from the start
		of each PPDU that are to be skipped before symbols take part in analysis. \n
			:return: num_data_symbols: integer Range: 0 to 10000"""
		response = self._core.io.query_str(f'SENSe:DEMod:FORMat:BANalyze:SYMBols:OFFSet?')
		return Conversions.str_to_float(response)
