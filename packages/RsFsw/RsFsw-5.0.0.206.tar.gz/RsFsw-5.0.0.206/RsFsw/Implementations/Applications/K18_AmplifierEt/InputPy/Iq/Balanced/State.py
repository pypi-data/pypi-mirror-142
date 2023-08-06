from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:IQ:BALanced[:STATe] \n
		Snippet: driver.applications.k18AmplifierEt.inputPy.iq.balanced.state.set(state = False, inputIx = repcap.InputIx.Default) \n
		This command defines whether the input is provided as a differential signal via all 4 Analog Baseband connectors or as a
		plain I/Q signal via 2 single-ended lines. \n
			:param state: ON | OFF | 1 | 0 ON | 1 Differential OFF | 0 Single ended
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.bool_to_str(state)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:IQ:BALanced:STATe {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> bool:
		"""SCPI: INPut<ip>:IQ:BALanced[:STATe] \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.inputPy.iq.balanced.state.get(inputIx = repcap.InputIx.Default) \n
		This command defines whether the input is provided as a differential signal via all 4 Analog Baseband connectors or as a
		plain I/Q signal via 2 single-ended lines. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: state: ON | OFF | 1 | 0 ON | 1 Differential OFF | 0 Single ended"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:IQ:BALanced:STATe?')
		return Conversions.str_to_bool(response)
