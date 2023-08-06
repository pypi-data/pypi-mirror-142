from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class McsIndex:
	"""McsIndex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcsIndex", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:BURSt:MCSindex \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.burst.mcsIndex.get() \n
		Queries the Modulation and Coding Scheme (MCS) index of the first analyzed PPDU. \n
			:return: mcs_index: No help available"""
		response = self._core.io.query_str(f'FETCh:BURSt:MCSindex?')
		return trim_str_response(response)
