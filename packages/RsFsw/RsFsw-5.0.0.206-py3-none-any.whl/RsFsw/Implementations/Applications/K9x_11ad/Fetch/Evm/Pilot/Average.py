from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def get(self) -> float:
		"""SCPI: FETCh:EVM:PILot:AVERage \n
		Snippet: value: float = driver.applications.k9X11Ad.fetch.evm.pilot.average.get() \n
		This command returns the average, maximum or minimum EVM for pilot symbols for the PPDU in dB. For details see 'EVM Pilot
		Symbols [dB]'. \n
			:return: result: No help available"""
		response = self._core.io.query_str(f'FETCh:EVM:PILot:AVERage?')
		return Conversions.str_to_float(response)
