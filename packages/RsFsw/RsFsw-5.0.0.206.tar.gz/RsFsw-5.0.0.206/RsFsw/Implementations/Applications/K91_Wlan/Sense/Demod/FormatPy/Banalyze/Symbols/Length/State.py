from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DEMod:FORMat:BANalyze:SYMBols:LENGth:STATe \n
		Snippet: driver.applications.k91Wlan.sense.demod.formatPy.banalyze.symbols.length.state.set(state = False) \n
		For IEEE 802.11a, ac, g (OFDM) , j, n, p signals only: If enabled, the number of PPDU data symbols after the 'Analysis
		Interval Offset' which are to be analyzed can be specified (see [SENSe:]DEMod:FORMat:BANalyze:SYMBols:LENGth) .
		If disabled, all PPDU data symbols after the 'Analysis Interval Offset' are evaluated. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DEMod:FORMat:BANalyze:SYMBols:LENGth:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DEMod:FORMat:BANalyze:SYMBols:LENGth:STATe \n
		Snippet: value: bool = driver.applications.k91Wlan.sense.demod.formatPy.banalyze.symbols.length.state.get() \n
		For IEEE 802.11a, ac, g (OFDM) , j, n, p signals only: If enabled, the number of PPDU data symbols after the 'Analysis
		Interval Offset' which are to be analyzed can be specified (see [SENSe:]DEMod:FORMat:BANalyze:SYMBols:LENGth) .
		If disabled, all PPDU data symbols after the 'Analysis Interval Offset' are evaluated. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'SENSe:DEMod:FORMat:BANalyze:SYMBols:LENGth:STATe?')
		return Conversions.str_to_bool(response)
