from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Update:
	"""Update commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("update", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: SYSTem:DISPlay:UPDate \n
		Snippet: driver.system.display.update.set(state = False) \n
		This command turns the display during remote operation on and off. If on, the R&S FSW updates the diagrams, traces and
		display fields only. The best performance is obtained if the display is off during remote control operation. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SYSTem:DISPlay:UPDate {param}')

	def get(self) -> bool:
		"""SCPI: SYSTem:DISPlay:UPDate \n
		Snippet: value: bool = driver.system.display.update.get() \n
		This command turns the display during remote operation on and off. If on, the R&S FSW updates the diagrams, traces and
		display fields only. The best performance is obtained if the display is off during remote control operation. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SYSTem:DISPlay:UPDate?')
		return Conversions.str_to_bool(response)
