from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Address:
	"""Address commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("address", core, parent)

	def set(self, address: str) -> None:
		"""SCPI: SYSTem:COMMunicate:TCPip:RDEVice:GENerator:ADDRess \n
		Snippet: driver.applications.k30NoiseFigure.system.communicate.tcpip.rdevice.generator.address.set(address = '1') \n
		Configures the TCP/IP address for the external generator. This command is only valid if External Generator Control (R&S
		FSW-B10) is installed. \n
			:param address: TCP/IP address between 0.0.0.0 and 0.255.255.255
		"""
		param = Conversions.value_to_quoted_str(address)
		self._core.io.write(f'SYSTem:COMMunicate:TCPip:RDEVice:GENerator:ADDRess {param}')

	def get(self) -> str:
		"""SCPI: SYSTem:COMMunicate:TCPip:RDEVice:GENerator:ADDRess \n
		Snippet: value: str = driver.applications.k30NoiseFigure.system.communicate.tcpip.rdevice.generator.address.get() \n
		Configures the TCP/IP address for the external generator. This command is only valid if External Generator Control (R&S
		FSW-B10) is installed. \n
			:return: address: TCP/IP address between 0.0.0.0 and 0.255.255.255"""
		response = self._core.io.query_str(f'SYSTem:COMMunicate:TCPip:RDEVice:GENerator:ADDRess?')
		return trim_str_response(response)
