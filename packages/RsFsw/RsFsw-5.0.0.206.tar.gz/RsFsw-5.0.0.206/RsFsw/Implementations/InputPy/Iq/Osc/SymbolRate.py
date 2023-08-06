from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SymbolRate:
	"""SymbolRate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbolRate", core, parent)

	def set(self, sample_rate: float, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:IQ:OSC:SRATe \n
		Snippet: driver.inputPy.iq.osc.symbolRate.set(sample_rate = 1.0, inputIx = repcap.InputIx.Default) \n
		Returns the used oscilloscope acquisition sample rate, which depends on the used I/Q mode (see method RsFsw.Applications.
		K149_Uwb.InputPy.Iq.Osc.TypePy.set) . \n
			:param sample_rate: 10 GHz | 20 GHz 10 GHz differential mode 20 GHz single-ended mode Unit: Hz
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.decimal_value_to_str(sample_rate)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:IQ:OSC:SRATe {param}')

	def get(self, inputIx=repcap.InputIx.Default) -> float:
		"""SCPI: INPut<ip>:IQ:OSC:SRATe \n
		Snippet: value: float = driver.inputPy.iq.osc.symbolRate.get(inputIx = repcap.InputIx.Default) \n
		Returns the used oscilloscope acquisition sample rate, which depends on the used I/Q mode (see method RsFsw.Applications.
		K149_Uwb.InputPy.Iq.Osc.TypePy.set) . \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: sample_rate: 10 GHz | 20 GHz 10 GHz differential mode 20 GHz single-ended mode Unit: Hz"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:IQ:OSC:SRATe?')
		return Conversions.str_to_float(response)
