from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:UPORt:STATe \n
		Snippet: driver.inputPy.uport.state.set(state = False, inputIx = repcap.InputIx.Default) \n
		This command toggles the control lines of the user ports for the AUX PORT connector. This 9-pole SUB-D male connector is
		located on the rear panel of the R&S FSW. See 'Aux. Port' for details. \n
			:param state: ON | 1 User port is switched to INPut OFF | 0 User port is switched to OUTPut
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.bool_to_str(state)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:UPORt:STATe {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> bool:
		"""SCPI: INPut<ip>:UPORt:STATe \n
		Snippet: value: bool = driver.inputPy.uport.state.get(inputIx = repcap.InputIx.Default) \n
		This command toggles the control lines of the user ports for the AUX PORT connector. This 9-pole SUB-D male connector is
		located on the rear panel of the R&S FSW. See 'Aux. Port' for details. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: state: ON | 1 User port is switched to INPut OFF | 0 User port is switched to OUTPut"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:UPORt:STATe?')
		return Conversions.str_to_bool(response)
