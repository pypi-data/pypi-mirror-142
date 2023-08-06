from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Display:
	"""Display commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("display", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: SYSTem:ERRor:DISPlay \n
		Snippet: driver.system.error.display.set(state = False) \n
		This command the error display during remote operation on and off. If activated, the R&S FSW displays a message box at
		the bottom of the screen that contains the most recent type of error and the command that caused the error. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SYSTem:ERRor:DISPlay {param}')

	def get(self) -> bool:
		"""SCPI: SYSTem:ERRor:DISPlay \n
		Snippet: value: bool = driver.system.error.display.get() \n
		This command the error display during remote operation on and off. If activated, the R&S FSW displays a message box at
		the bottom of the screen that contains the most recent type of error and the command that caused the error. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SYSTem:ERRor:DISPlay?')
		return Conversions.str_to_bool(response)
