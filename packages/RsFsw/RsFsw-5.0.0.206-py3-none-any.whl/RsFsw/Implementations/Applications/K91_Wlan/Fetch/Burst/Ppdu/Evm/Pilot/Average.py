from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Average:
	"""Average commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("average", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:BURSt:PPDU:EVM:PILot:AVERage \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.burst.ppdu.evm.pilot.average.get() \n
		Returns the error vector magnitude results for each PPDU, averaged over all pilot subcarriers for all symbols and streams. \n
			:return: result: Comma-separated list of EVM values, one for each PPDU Unit: dB"""
		response = self._core.io.query_str(f'FETCh:BURSt:PPDU:EVM:PILot:AVERage?')
		return trim_str_response(response)
