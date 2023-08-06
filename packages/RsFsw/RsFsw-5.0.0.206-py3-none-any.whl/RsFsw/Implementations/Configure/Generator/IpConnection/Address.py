from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Address:
	"""Address commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("address", core, parent)

	def set(self, ip_address: str) -> None:
		"""SCPI: CONFigure:GENerator:IPConnection:ADDRess \n
		Snippet: driver.configure.generator.ipConnection.address.set(ip_address = '1') \n
		The TCPIP address or computer name of the signal generator connected to the R&S FSW via LAN. The IP address / computer
		name is maintained after a [PRESET], and is transferred between applications. \n
			:param ip_address: IP address or computer name
		"""
		param = Conversions.value_to_quoted_str(ip_address)
		self._core.io.write(f'CONFigure:GENerator:IPConnection:ADDRess {param}')

	def get(self) -> str:
		"""SCPI: CONFigure:GENerator:IPConnection:ADDRess \n
		Snippet: value: str = driver.configure.generator.ipConnection.address.get() \n
		The TCPIP address or computer name of the signal generator connected to the R&S FSW via LAN. The IP address / computer
		name is maintained after a [PRESET], and is transferred between applications. \n
			:return: ip_address: IP address or computer name"""
		response = self._core.io.query_str(f'CONFigure:GENerator:IPConnection:ADDRess?')
		return trim_str_response(response)
