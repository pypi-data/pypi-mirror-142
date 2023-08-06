from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:GAIN:STATe \n
		Snippet: driver.applications.k70Vsa.inputPy.gain.state.set(state = False, inputIx = repcap.InputIx.Default) \n
		This command turns the internal preamplifier on and off. It requires the optional preamplifier hardware. Note that if an
		optional external preamplifier is activated, the internal preamplifier is automatically disabled, and vice versa.
		This function is not available for input from the optional Digital Baseband Interface. If option R&S FSW-B22 is installed,
		the preamplifier is only active below 7 GHz. If option R&S FSW-B24 is installed, the preamplifier is active for all
		frequencies. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.bool_to_str(state)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:GAIN:STATe {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> bool:
		"""SCPI: INPut<ip>:GAIN:STATe \n
		Snippet: value: bool = driver.applications.k70Vsa.inputPy.gain.state.get(inputIx = repcap.InputIx.Default) \n
		This command turns the internal preamplifier on and off. It requires the optional preamplifier hardware. Note that if an
		optional external preamplifier is activated, the internal preamplifier is automatically disabled, and vice versa.
		This function is not available for input from the optional Digital Baseband Interface. If option R&S FSW-B22 is installed,
		the preamplifier is only active below 7 GHz. If option R&S FSW-B24 is installed, the preamplifier is active for all
		frequencies. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:GAIN:STATe?')
		return Conversions.str_to_bool(response)
