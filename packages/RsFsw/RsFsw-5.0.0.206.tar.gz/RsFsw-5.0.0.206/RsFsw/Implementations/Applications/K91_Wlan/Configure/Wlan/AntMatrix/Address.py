from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Address:
	"""Address commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Antenna, default value after init: Antenna.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("address", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_antenna_get', 'repcap_antenna_set', repcap.Antenna.Nr1)

	def repcap_antenna_set(self, antenna: repcap.Antenna) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Antenna.Default
		Default value after init: Antenna.Nr1"""
		self._cmd_group.set_repcap_enum_value(antenna)

	def repcap_antenna_get(self) -> repcap.Antenna:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, address: str, antenna=repcap.Antenna.Default) -> None:
		"""SCPI: CONFigure:WLAN:ANTMatrix:ADDRess<ant> \n
		Snippet: driver.applications.k91Wlan.configure.wlan.antMatrix.address.set(address = '1', antenna = repcap.Antenna.Default) \n
		This remote control command specifies the TCP/IP address for each receiver path in IPV4 format. Note, it is not possible
		to set the IP address of ANTMatrix1 (primary) \n
			:param address: TCP/IP address in IPV4 format
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Address')
		"""
		param = Conversions.value_to_quoted_str(address)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		self._core.io.write(f'CONFigure:WLAN:ANTMatrix:ADDRess{antenna_cmd_val} {param}')

	def get(self, antenna=repcap.Antenna.Default) -> str:
		"""SCPI: CONFigure:WLAN:ANTMatrix:ADDRess<ant> \n
		Snippet: value: str = driver.applications.k91Wlan.configure.wlan.antMatrix.address.get(antenna = repcap.Antenna.Default) \n
		This remote control command specifies the TCP/IP address for each receiver path in IPV4 format. Note, it is not possible
		to set the IP address of ANTMatrix1 (primary) \n
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Address')
			:return: address: TCP/IP address in IPV4 format"""
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		response = self._core.io.query_str(f'CONFigure:WLAN:ANTMatrix:ADDRess{antenna_cmd_val}?')
		return trim_str_response(response)

	def clone(self) -> 'Address':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Address(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
