from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class All:
	"""All commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("all", core, parent)

	def get(self) -> int:
		"""SCPI: FETCh:BURSt:COUNt:ALL \n
		Snippet: value: int = driver.applications.k91Wlan.fetch.burst.count.all.get() \n
		This command returns the number of analyzed PPDUs for the entire measurement. If multiple measurements are required
		because the number of PPDUs to analyze is greater than the number of PPDUs that can be captured in one buffer, this
		command returns the number of analyzed PPDUs in all measurements (as opposed to method RsFsw.Applications.K91_Wlan.Fetch.
		Burst.Count.get_. \n
			:return: ppdu_count: No help available"""
		response = self._core.io.query_str(f'FETCh:BURSt:COUNt:ALL?')
		return Conversions.str_to_int(response)
