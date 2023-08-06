from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ginterval:
	"""Ginterval commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ginterval", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:BURSt:GINTerval \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.burst.ginterval.get() \n
		Queries the guard interval of the first analyzed PPDU. \n
			:return: guard_interval: Guard interval in microseconds."""
		response = self._core.io.query_str(f'FETCh:BURSt:GINTerval?')
		return trim_str_response(response)
