from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def get(self) -> float:
		"""SCPI: FETCh:BURSt:COUNt \n
		Snippet: value: float = driver.applications.k9X11Ad.fetch.burst.count.get() \n
		This command returns the number of analyzed PPDUs from the current capture buffer. \n
			:return: value: integer"""
		response = self._core.io.query_str(f'FETCh:BURSt:COUNt?')
		return Conversions.str_to_float(response)
