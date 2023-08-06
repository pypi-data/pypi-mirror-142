from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Starts:
	"""Starts commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("starts", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:BURSt:STARts \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.burst.starts.get() \n
		This command returns the start position of each analyzed PPDU in the current capture buffer. \n
			:return: position: list Comma-separated list of sample numbers indicating the start position of each PPDU. Tip: To obtain the result in seconds, divide the sample number by the input sample rate. This value is indicated as 'Sample Rate Fs' in the channel bar."""
		response = self._core.io.query_str(f'FETCh:BURSt:STARts?')
		return trim_str_response(response)
