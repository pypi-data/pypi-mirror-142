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
		"""SCPI: INPut:GAIN:STATe \n
		Snippet: driver.applications.k6Pulse.inputPy.gain.state.set(state = False) \n
		This command turns the internal preamplifier on and off. It requires the optional preamplifier hardware. Note that if an
		optional external preamplifier is activated, the internal preamplifier is automatically disabled, and vice versa. For R&S
		FSW 8 or 13 models, the preamplification is defined by method RsFsw.Applications.K10x_Lte.InputPy.Gain.Value.set. For R&S
		FSW 26 or higher models, the input signal is amplified by 30 dB if the preamplifier is activated. If option R&S FSW-B22
		is installed, the preamplifier is only active below 7 GHz. If option R&S FSW-B24 is installed, the preamplifier is active
		for all frequencies. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'INPut:GAIN:STATe {param}')

	def get(self) -> bool:
		"""SCPI: INPut:GAIN:STATe \n
		Snippet: value: bool = driver.applications.k6Pulse.inputPy.gain.state.get() \n
		This command turns the internal preamplifier on and off. It requires the optional preamplifier hardware. Note that if an
		optional external preamplifier is activated, the internal preamplifier is automatically disabled, and vice versa. For R&S
		FSW 8 or 13 models, the preamplification is defined by method RsFsw.Applications.K10x_Lte.InputPy.Gain.Value.set. For R&S
		FSW 26 or higher models, the input signal is amplified by 30 dB if the preamplifier is activated. If option R&S FSW-B22
		is installed, the preamplifier is only active below 7 GHz. If option R&S FSW-B24 is installed, the preamplifier is active
		for all frequencies. \n
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		response = self._core.io.query_str(f'INPut:GAIN:STATe?')
		return Conversions.str_to_bool(response)
