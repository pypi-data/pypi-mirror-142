from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Address:
	"""Address commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("address", core, parent)

	def set(self, address: str, generator=repcap.Generator.Default) -> None:
		"""SCPI: SYSTem:COMMunicate:TCPip:RDEVice:GENerator<gen>:ADDRess \n
		Snippet: driver.system.communicate.tcpip.rdevice.generator.address.set(address = '1', generator = repcap.Generator.Default) \n
		Configures the TCP/IP address for the external generator. This command is only valid if External Generator Control (R&S
		FSW-B10) is installed. \n
			:param address: TCP/IP address between 0.0.0.0 and 0.255.255.255
			:param generator: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Generator')
		"""
		param = Conversions.value_to_quoted_str(address)
		generator_cmd_val = self._cmd_group.get_repcap_cmd_value(generator, repcap.Generator)
		self._core.io.write(f'SYSTem:COMMunicate:TCPip:RDEVice:GENerator{generator_cmd_val}:ADDRess {param}')

	def get(self, generator=repcap.Generator.Default) -> str:
		"""SCPI: SYSTem:COMMunicate:TCPip:RDEVice:GENerator<gen>:ADDRess \n
		Snippet: value: str = driver.system.communicate.tcpip.rdevice.generator.address.get(generator = repcap.Generator.Default) \n
		Configures the TCP/IP address for the external generator. This command is only valid if External Generator Control (R&S
		FSW-B10) is installed. \n
			:param generator: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Generator')
			:return: address: TCP/IP address between 0.0.0.0 and 0.255.255.255"""
		generator_cmd_val = self._cmd_group.get_repcap_cmd_value(generator, repcap.Generator)
		response = self._core.io.query_str(f'SYSTem:COMMunicate:TCPip:RDEVice:GENerator{generator_cmd_val}:ADDRess?')
		return trim_str_response(response)
