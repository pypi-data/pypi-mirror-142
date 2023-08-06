from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: SYSTem:DISPlay:FPANel[:STATe] \n
		Snippet: driver.system.display.fpanel.state.set(state = False) \n
		This command includes or excludes the front panel keys when working with the remote desktop. \n
			:param state: ON | OFF | 0 | 1
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SYSTem:DISPlay:FPANel:STATe {param}')

	def get(self) -> bool:
		"""SCPI: SYSTem:DISPlay:FPANel[:STATe] \n
		Snippet: value: bool = driver.system.display.fpanel.state.get() \n
		This command includes or excludes the front panel keys when working with the remote desktop. \n
			:return: state: ON | OFF | 0 | 1"""
		response = self._core.io.query_str(f'SYSTem:DISPlay:FPANel:STATe?')
		return Conversions.str_to_bool(response)
