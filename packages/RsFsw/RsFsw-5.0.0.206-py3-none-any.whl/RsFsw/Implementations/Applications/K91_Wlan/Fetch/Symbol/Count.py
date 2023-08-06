from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def get(self) -> str:
		"""SCPI: FETCh:SYMBol:COUNt \n
		Snippet: value: str = driver.applications.k91Wlan.fetch.symbol.count.get() \n
		This command returns the number of symbols in each analyzed PPDU as a comma-separated list. The length of the list
		corresponds to the number of PPDUs, i.e. the result of method RsFsw.Applications.K91_Wlan.Fetch.Burst.Count.All.get_. \n
			:return: result: list"""
		response = self._core.io.query_str(f'FETCh:SYMBol:COUNt?')
		return trim_str_response(response)
