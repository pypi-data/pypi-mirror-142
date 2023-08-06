from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DIRected:INPut:GAIN:STATe \n
		Snippet: driver.applications.k50Spurious.sense.directed.inputPy.gain.state.set(state = False) \n
		Switches the optional preamplifier on or off (if available) for the directed search measurement. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DIRected:INPut:GAIN:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DIRected:INPut:GAIN:STATe \n
		Snippet: value: bool = driver.applications.k50Spurious.sense.directed.inputPy.gain.state.get() \n
		Switches the optional preamplifier on or off (if available) for the directed search measurement. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'SENSe:DIRected:INPut:GAIN:STATe?')
		return Conversions.str_to_bool(response)
