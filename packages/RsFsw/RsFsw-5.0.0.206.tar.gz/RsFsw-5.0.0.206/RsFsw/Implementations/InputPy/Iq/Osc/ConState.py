from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConState:
	"""ConState commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("conState", core, parent)

	def get(self, inputIx=repcap.InputIx.Default) -> float:
		"""SCPI: INPut<ip>:IQ:OSC:CONState \n
		Snippet: value: float = driver.inputPy.iq.osc.conState.get(inputIx = repcap.InputIx.Default) \n
		Returns the state of the LAN connection to the oscilloscope for the optional Oscilloscope Baseband Input. For details see
		'Processing Oscilloscope Baseband Input'. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: connection_state: CONNECTED | NOT_CONNECTED | ESTABLISHING_CONNECTION CONNECTED Connection to the instrument has been established successfully. ESTABLISHING_CONNECTION Connection is currently being established. NOT_CONNECTED Connection to the instrument could not be established. Check the connection between the R&S FSW and the oscilloscope, and make sure the IP address of the oscilloscope has been defined (see method RsFsw.Applications.K149_Uwb.InputPy.Iq.Osc.Tcpip.set) ."""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:IQ:OSC:CONState?')
		return Conversions.str_to_float(response)
