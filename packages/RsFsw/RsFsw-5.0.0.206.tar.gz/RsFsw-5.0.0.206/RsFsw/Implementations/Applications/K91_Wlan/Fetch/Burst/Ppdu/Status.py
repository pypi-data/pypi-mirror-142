from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Status:
	"""Status commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("status", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:BURSt:PPDU:STATus \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.burst.ppdu.status.get() \n
		Queries the status of the analyzed PPDUs in the current capture buffer (see method RsFsw.Applications.K91_Wlan.Fetch.
		Burst.Count.get_) . \n
			:return: result: Comma-separated list of values; one value for each analyzed PPDU OK Analysis correct WARN Warning, an error occurred SEL Selected PPDU"""
		response = self._core.io.query_str(f'FETCh:BURSt:PPDU:STATus?')
		return trim_str_response(response)
