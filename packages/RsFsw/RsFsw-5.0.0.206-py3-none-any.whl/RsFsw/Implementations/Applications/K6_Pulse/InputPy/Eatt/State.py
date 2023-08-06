from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: INPut:EATT:STATe \n
		Snippet: driver.applications.k6Pulse.inputPy.eatt.state.set(state = False) \n
		This command turns the electronic attenuator on and off. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'INPut:EATT:STATe {param}')

	def get(self) -> bool:
		"""SCPI: INPut:EATT:STATe \n
		Snippet: value: bool = driver.applications.k6Pulse.inputPy.eatt.state.get() \n
		This command turns the electronic attenuator on and off. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'INPut:EATT:STATe?')
		return Conversions.str_to_bool(response)
