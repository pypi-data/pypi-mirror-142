from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Enable:
	"""Enable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enable", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: SYSTem:COMMunicate:REST:ENABle \n
		Snippet: driver.system.communicate.rest.enable.set(state = False) \n
		This command turns communication via the REST API on and off. \n
			:param state: ON | OFF | 0 | 1
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SYSTem:COMMunicate:REST:ENABle {param}')

	def get(self) -> bool:
		"""SCPI: SYSTem:COMMunicate:REST:ENABle \n
		Snippet: value: bool = driver.system.communicate.rest.enable.get() \n
		This command turns communication via the REST API on and off. \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:REST:ENABle?')
		return Conversions.str_to_bool(response)
