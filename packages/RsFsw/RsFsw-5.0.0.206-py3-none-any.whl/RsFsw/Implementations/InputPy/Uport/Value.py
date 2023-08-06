from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def get(self, inputIx=repcap.InputIx.Default) -> float:
		"""SCPI: INPut<ip>:UPORt[:VALue] \n
		Snippet: value: float = driver.inputPy.uport.value.get(inputIx = repcap.InputIx.Default) \n
		This command queries the control lines of the user ports. For details see method RsFsw.Output.Uport.Value.set. \n
			:param inputIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'InputPy')
			:return: level: bit values in hexadecimal format TTL type voltage levels (max. 5V) Range: #B00000000 to #B00111111"""
		inputIx_cmd_val = self._cmd_group.get_repcap_cmd_value(inputIx, repcap.InputIx)
		response = self._core.io.query_str(f'INPut{inputIx_cmd_val}:UPORt:VALue?')
		return Conversions.str_to_float(response)
