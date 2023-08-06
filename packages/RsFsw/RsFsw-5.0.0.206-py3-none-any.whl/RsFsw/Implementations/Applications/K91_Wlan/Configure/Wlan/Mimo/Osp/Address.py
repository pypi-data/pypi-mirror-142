from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Address:
	"""Address commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("address", core, parent)

	def set(self, address: str) -> None:
		"""SCPI: CONFigure:WLAN:MIMO:OSP:ADDRess \n
		Snippet: driver.applications.k91Wlan.configure.wlan.mimo.osp.address.set(address = '1') \n
		Specifies the TCP/IP address of the switch unit to be used for automated sequential MIMO measurements. The supported unit
		is Rohde & Schwarz OSP 1505.3009.03 with module option 1505.5101.02 \n
			:param address: No help available
		"""
		param = Conversions.value_to_quoted_str(address)
		self._core.io.write(f'CONFigure:WLAN:MIMO:OSP:ADDRess {param}')

	def get(self) -> str:
		"""SCPI: CONFigure:WLAN:MIMO:OSP:ADDRess \n
		Snippet: value: str = driver.applications.k91Wlan.configure.wlan.mimo.osp.address.get() \n
		Specifies the TCP/IP address of the switch unit to be used for automated sequential MIMO measurements. The supported unit
		is Rohde & Schwarz OSP 1505.3009.03 with module option 1505.5101.02 \n
			:return: address: No help available"""
		response = self._core.io.query_str(f'CONFigure:WLAN:MIMO:OSP:ADDRess?')
		return trim_str_response(response)
