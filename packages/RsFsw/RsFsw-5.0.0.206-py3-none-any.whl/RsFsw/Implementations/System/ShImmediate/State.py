from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: SYSTem:SHIMmediate:STATe \n
		Snippet: driver.system.shImmediate.state.set(state = False) \n
		Determines when the remote commands that change hardware settings on the R&S FSW are executed. Regardless of this setting,
		the firmware automatically sets the hardware when a sweep is started. This setting is not changed by the preset function. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Remote commands that cause changes to the hardware are only executed when the SYSTem:SHIMmediate ONCE command is executed. ON | 1 Remote commands are always executed immediately when they are received by the instrument.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SYSTem:SHIMmediate:STATe {param}')

	def get(self) -> bool:
		"""SCPI: SYSTem:SHIMmediate:STATe \n
		Snippet: value: bool = driver.system.shImmediate.state.get() \n
		Determines when the remote commands that change hardware settings on the R&S FSW are executed. Regardless of this setting,
		the firmware automatically sets the hardware when a sweep is started. This setting is not changed by the preset function. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Remote commands that cause changes to the hardware are only executed when the SYSTem:SHIMmediate ONCE command is executed. ON | 1 Remote commands are always executed immediately when they are received by the instrument."""
		response = self._core.io.query_str(f'SYSTem:SHIMmediate:STATe?')
		return Conversions.str_to_bool(response)
