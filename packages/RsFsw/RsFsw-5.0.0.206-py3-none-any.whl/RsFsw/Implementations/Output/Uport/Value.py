from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, value: str, outputConnector=repcap.OutputConnector.Default) -> None:
		"""SCPI: OUTPut<up>:UPORt[:VALue] \n
		Snippet: driver.output.uport.value.set(value = r1, outputConnector = repcap.OutputConnector.Default) \n
		This command sets the control lines of the user ports. The assignment of the pin numbers to the bits is as follows:
			Table Header: Bit / 7 / 6 / 5 / 4 / 3 / 2 / 1 / 0 \n
			- Pin / N/A / N/A / 5 / 3 / 4 / 7 / 6 / 2
		Bits 7 and 6 are not assigned to pins and must always be 0. The user port is written to with the given binary pattern. If
		the user port is programmed to input instead of output (see method RsFsw.InputPy.Uport.State.set) , the output value is
		temporarily stored. \n
			:param value: bit values in hexadecimal format TTL type voltage levels (max. 5V) Range: #B00000000 to #B00111111
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.value_to_str(value)
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		self._core.io.write(f'OUTPut{outputConnector_cmd_val}:UPORt:VALue {param}')

	def get(self, outputConnector=repcap.OutputConnector.Default) -> str:
		"""SCPI: OUTPut<up>:UPORt[:VALue] \n
		Snippet: value: str = driver.output.uport.value.get(outputConnector = repcap.OutputConnector.Default) \n
		This command sets the control lines of the user ports. The assignment of the pin numbers to the bits is as follows:
			Table Header: Bit / 7 / 6 / 5 / 4 / 3 / 2 / 1 / 0 \n
			- Pin / N/A / N/A / 5 / 3 / 4 / 7 / 6 / 2
		Bits 7 and 6 are not assigned to pins and must always be 0. The user port is written to with the given binary pattern. If
		the user port is programmed to input instead of output (see method RsFsw.InputPy.Uport.State.set) , the output value is
		temporarily stored. \n
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: value: bit values in hexadecimal format TTL type voltage levels (max. 5V) Range: #B00000000 to #B00111111"""
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		response = self._core.io.query_str(f'OUTPut{outputConnector_cmd_val}:UPORt:VALue?')
		return trim_str_response(response)
