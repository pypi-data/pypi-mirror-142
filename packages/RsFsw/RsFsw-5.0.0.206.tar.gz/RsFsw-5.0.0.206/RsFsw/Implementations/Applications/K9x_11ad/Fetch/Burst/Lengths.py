from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lengths:
	"""Lengths commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lengths", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:BURSt:LENGths \n
		Snippet: value: str = driver.applications.k9X11Ad.fetch.burst.lengths.get() \n
		This command returns the EVM symbol count of the analyzed PPDUs from the current measurement.
		The result is a comma-separated list of symbol counts, one for each PPDU. \n
			:return: ppdu_length: integer value number of symbols as counted for the EVM calculation"""
		response = self._core.io.query_str(f'FETCh:BURSt:LENGths?')
		return trim_str_response(response)
