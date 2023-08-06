from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ptype:
	"""Ptype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ptype", core, parent)

	def set(self, pad_type: enums.PadType, inputIx=repcap.InputIx.Default) -> None:
		"""SCPI: INPut<ip>:IQ:IMPedance:PTYPe \n
		Snippet: driver.inputPy.iq.impedance.ptype.set(pad_type = enums.PadType.MLPad, inputIx = repcap.InputIx.Default) \n
		Defines the type of matching pad used for impedance conversion for analog baseband input. For RF input, use the method
		RsFsw.InputPy.Impedance.Ptype.set command. \n
			:param pad_type: SRESistor | MLPad SRESistor Series-R MLPad Minimum Loss Pad
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
		"""
		param = Conversions.enum_scalar_to_str(pad_type, enums.PadType)
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		self._core.io.write(f'INPut{inputIx_cmd_val}:IQ:IMPedance:PTYPe {param}')

	# noinspection PyTypeChecker
	def get(self, inputIx=repcap.InputIx.Default) -> enums.PadType:
		"""SCPI: INPut<ip>:IQ:IMPedance:PTYPe \n
		Snippet: value: enums.PadType = driver.inputPy.iq.impedance.ptype.get(inputIx = repcap.InputIx.Default) \n
		Defines the type of matching pad used for impedance conversion for analog baseband input. For RF input, use the method
		RsFsw.InputPy.Impedance.Ptype.set command. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: pad_type: SRESistor | MLPad SRESistor Series-R MLPad Minimum Loss Pad"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:IQ:IMPedance:PTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.PadType)
