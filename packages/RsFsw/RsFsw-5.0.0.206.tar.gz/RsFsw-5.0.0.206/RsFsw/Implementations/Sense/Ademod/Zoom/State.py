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
		"""SCPI: [SENSe]:ADEMod:ZOOM[:STATe] \n
		Snippet: driver.sense.ademod.zoom.state.set(state = False) \n
		The command enables or disables the time domain zoom function for the analog-demodulated measurement data in the
		specified window. If the zoom function is enabled, the defined number of sweep points are displayed from the start time
		specified with [SENSe:]ADEMod<n>:ZOOM:STARt. If the zoom function is disabled, data reduction is used to adapt the
		measurement points to the number of points available on the display. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:ADEMod:ZOOM:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:ADEMod:ZOOM[:STATe] \n
		Snippet: value: bool = driver.sense.ademod.zoom.state.get() \n
		The command enables or disables the time domain zoom function for the analog-demodulated measurement data in the
		specified window. If the zoom function is enabled, the defined number of sweep points are displayed from the start time
		specified with [SENSe:]ADEMod<n>:ZOOM:STARt. If the zoom function is disabled, data reduction is used to adapt the
		measurement points to the number of points available on the display. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'SENSe:ADEMod:ZOOM:STATe?')
		return Conversions.str_to_bool(response)
