from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lock:
	"""Lock commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lock", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: SYSTem:DISPlay:LOCK \n
		Snippet: driver.system.display.lock.set(state = False) \n
		Defines whether the 'Display Update' function remains available in remote operation or not. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 The function remains available. ON | 1 The function is not available and the display is not updated during remote operation.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SYSTem:DISPlay:LOCK {param}')

	def get(self) -> bool:
		"""SCPI: SYSTem:DISPlay:LOCK \n
		Snippet: value: bool = driver.system.display.lock.get() \n
		Defines whether the 'Display Update' function remains available in remote operation or not. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 The function remains available. ON | 1 The function is not available and the display is not updated during remote operation."""
		response = self._core.io.query_str(f'SYSTem:DISPlay:LOCK?')
		return Conversions.str_to_bool(response)
