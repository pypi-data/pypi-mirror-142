from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:SFSummary:ALL \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.sfSummary.all.get() \n
		Returns the numeric results of the Spectrum Flatness trace. This command is only available for the IEEE 802.11ax standard.
		For details see 'Spectrum Flatness Result Summary'. \n
			:return: result: SC_Start_No,SC_End_No,MinDist_Low,SC_MinDist_Low,MinDist_Up,SC_MinDist_Up,LimitCheckResult,... Comma-separated list of values for the overall subcarrier range and each subrange."""
		response = self._core.io.query_str(f'FETCh:SFSummary:ALL?')
		return trim_str_response(response)
