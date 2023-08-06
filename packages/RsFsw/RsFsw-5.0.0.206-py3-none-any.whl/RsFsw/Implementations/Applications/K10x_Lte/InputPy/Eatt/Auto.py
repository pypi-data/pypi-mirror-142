from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool, inputIx=repcap.InputIx.Default, instrument=repcap.Instrument.Default) -> None:
		"""SCPI: INPut<ip>:EATT<ant>:AUTO \n
		Snippet: driver.applications.k10Xlte.inputPy.eatt.auto.set(state = False, inputIx = repcap.InputIx.Default, instrument = repcap.Instrument.Default) \n
		This command turns automatic selection of the electronic attenuation on and off. If on, electronic attenuation reduces
		the mechanical attenuation whenever possible. This command is available with the optional Electronic Attenuator, but not
		if you are using the optional Digital Baseband Input. \n
			:param state: ON | OFF | 1 | 0
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:param instrument: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Eatt')
		"""
		param = Conversions.bool_to_str(state)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		instrument_cmd_val = self._cmd_group.get_repcap_cmd_value(instrument, repcap.Instrument)
		self._core.io.write(f'INPut{inputIx_cmd_val}:EATT{instrument_cmd_val}:AUTO {param}')

	def get(self, inputIx=repcap.InputIx.Default, instrument=repcap.Instrument.Default) -> bool:
		"""SCPI: INPut<ip>:EATT<ant>:AUTO \n
		Snippet: value: bool = driver.applications.k10Xlte.inputPy.eatt.auto.get(inputIx = repcap.InputIx.Default, instrument = repcap.Instrument.Default) \n
		This command turns automatic selection of the electronic attenuation on and off. If on, electronic attenuation reduces
		the mechanical attenuation whenever possible. This command is available with the optional Electronic Attenuator, but not
		if you are using the optional Digital Baseband Input. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:param instrument: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Eatt')
			:return: state: ON | OFF | 1 | 0"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		instrument_cmd_val = self._cmd_group.get_repcap_cmd_value(instrument, repcap.Instrument)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:EATT{instrument_cmd_val}:AUTO?')
		return Conversions.str_to_bool(response)
