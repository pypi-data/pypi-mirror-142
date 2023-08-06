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
		"""SCPI: [SENSe]:ADEMod:SETTling:TIME:STATe \n
		Snippet: driver.sense.ademod.settling.time.state.set(state = False) \n
		Enables or disables the calculation and display of the settling time. The function is available for all time domain
		displays. For details, see 'Settling time'. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:ADEMod:SETTling:TIME:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:ADEMod:SETTling:TIME:STATe \n
		Snippet: value: bool = driver.sense.ademod.settling.time.state.get() \n
		Enables or disables the calculation and display of the settling time. The function is available for all time domain
		displays. For details, see 'Settling time'. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'SENSe:ADEMod:SETTling:TIME:STATe?')
		return Conversions.str_to_bool(response)
