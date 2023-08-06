from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tcpip:
	"""Tcpip commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tcpip", core, parent)

	def set(self, tcpip: str, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:IQ:OSC:TCPip \n
		Snippet: driver.inputPy.iq.osc.tcpip.set(tcpip = '1', inputIx = repcap.InputIx.Default) \n
		Defines the TCPIP address or computer name of the oscilloscope connected to the R&S FSW via LAN. Note: The IP address is
		maintained after a [PRESET], and is transferred between applications. \n
			:param tcpip: computer name or IP address
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.value_to_quoted_str(tcpip)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:IQ:OSC:TCPip {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> str:
		"""SCPI: INPut<ip>:IQ:OSC:TCPip \n
		Snippet: value: str = driver.inputPy.iq.osc.tcpip.get(inputIx = repcap.InputIx.Default) \n
		Defines the TCPIP address or computer name of the oscilloscope connected to the R&S FSW via LAN. Note: The IP address is
		maintained after a [PRESET], and is transferred between applications. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: tcpip: computer name or IP address"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:IQ:OSC:TCPip?')
		return trim_str_response(response)
