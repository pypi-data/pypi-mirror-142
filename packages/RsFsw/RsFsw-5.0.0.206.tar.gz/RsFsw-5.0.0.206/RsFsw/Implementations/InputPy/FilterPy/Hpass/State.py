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
		"""SCPI: INPut:FILTer:HPASs[:STATe] \n
		Snippet: driver.inputPy.filterPy.hpass.state.set(state = False) \n
		Activates an additional internal high-pass filter for RF input signals from 1 GHz to 3 GHz. This filter is used to remove
		the harmonics of the R&S FSW in order to measure the harmonics for a DUT, for example. This function requires an
		additional high-pass filter hardware option. (Note: for RF input signals outside the specified range, the high-pass
		filter has no effect. For signals with a frequency of approximately 4 GHz upwards, the harmonics are suppressed
		sufficiently by the YIG-preselector, if available.) \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'INPut:FILTer:HPASs:STATe {param}')

	def get(self) -> bool:
		"""SCPI: INPut:FILTer:HPASs[:STATe] \n
		Snippet: value: bool = driver.inputPy.filterPy.hpass.state.get() \n
		Activates an additional internal high-pass filter for RF input signals from 1 GHz to 3 GHz. This filter is used to remove
		the harmonics of the R&S FSW in order to measure the harmonics for a DUT, for example. This function requires an
		additional high-pass filter hardware option. (Note: for RF input signals outside the specified range, the high-pass
		filter has no effect. For signals with a frequency of approximately 4 GHz upwards, the harmonics are suppressed
		sufficiently by the YIG-preselector, if available.) \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'INPut:FILTer:HPASs:STATe?')
		return Conversions.str_to_bool(response)
