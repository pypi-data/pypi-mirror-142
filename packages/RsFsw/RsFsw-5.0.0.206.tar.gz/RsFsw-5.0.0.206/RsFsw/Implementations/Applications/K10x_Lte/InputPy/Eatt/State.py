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

	def set(self, state: bool, inputIx=repcap.InputIx.Default, instrument=repcap.Instrument.Default) -> None:
		"""SCPI: INPut<ip>:EATT<ant>:STATe \n
		Snippet: driver.applications.k10Xlte.inputPy.eatt.state.set(state = False, inputIx = repcap.InputIx.Default, instrument = repcap.Instrument.Default) \n
		This command turns the electronic attenuator on and off. This command is available with the optional Electronic
		Attenuator, but not if you are using the optional Digital Baseband Input. \n
			:param state: ON | OFF
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:param instrument: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Eatt')
		"""
		param = Conversions.bool_to_str(state)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		instrument_cmd_val = self._cmd_group.get_repcap_cmd_value(instrument, repcap.Instrument)
		self._core.io.write(f'INPut{inputIx_cmd_val}:EATT{instrument_cmd_val}:STATe {param}')

	def get(self, inputIx=repcap.InputIx.Default, instrument=repcap.Instrument.Default) -> bool:
		"""SCPI: INPut<ip>:EATT<ant>:STATe \n
		Snippet: value: bool = driver.applications.k10Xlte.inputPy.eatt.state.get(inputIx = repcap.InputIx.Default, instrument = repcap.Instrument.Default) \n
		This command turns the electronic attenuator on and off. This command is available with the optional Electronic
		Attenuator, but not if you are using the optional Digital Baseband Input. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:param instrument: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Eatt')
			:return: state: ON | OFF"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		instrument_cmd_val = self._cmd_group.get_repcap_cmd_value(instrument, repcap.Instrument)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:EATT{instrument_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
