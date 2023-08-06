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
		"""SCPI: INPut:FILTer:YIG[:STATe] \n
		Snippet: driver.inputPy.filterPy.yig.state.set(state = False) \n
		Enables or disables the YIG filter. \n
			:param state: ON | OFF | 0 | 1
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'INPut:FILTer:YIG:STATe {param}')

	def get(self) -> bool:
		"""SCPI: INPut:FILTer:YIG[:STATe] \n
		Snippet: value: bool = driver.inputPy.filterPy.yig.state.get() \n
		Enables or disables the YIG filter. \n
			:return: state: ON | OFF | 0 | 1"""
		response = self._core.io.query_str(f'INPut:FILTer:YIG:STATe?')
		return Conversions.str_to_bool(response)
