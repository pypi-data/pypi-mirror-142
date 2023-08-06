from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Antenna:
	"""Antenna commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Antenna, default value after init: Antenna.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("antenna", core, parent)
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

	def set(self, receiver_antenna: enums.AntennaA, antenna=repcap.Antenna.Default) -> None:
		"""SCPI: CONFigure:WLAN:ANTMatrix:ANTenna<ant> \n
		Snippet: driver.applications.k91Wlan.configure.wlan.antMatrix.antenna.set(receiver_antenna = enums.AntennaA.ANT1, antenna = repcap.Antenna.Default) \n
		This remote control command specifies the antenna assignment of the receive path. \n
			:param receiver_antenna: ANTenna1 | ANTenna2 | ANTenna3 | ANTenna4 | ANTenna5 | ANTenna6 | ANTenna7 | ANTenna8 | ANT1 | ANT2 | ANT3 | ANT4 | ANT5 | ANT6 | ANT7 | ANT8 Antenna assignment of the receiver path
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Antenna')
		"""
		param = Conversions.enum_scalar_to_str(receiver_antenna, enums.AntennaA)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		self._core.io.write(f'CONFigure:WLAN:ANTMatrix:ANTenna{antenna_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, antenna=repcap.Antenna.Default) -> enums.AntennaA:
		"""SCPI: CONFigure:WLAN:ANTMatrix:ANTenna<ant> \n
		Snippet: value: enums.AntennaA = driver.applications.k91Wlan.configure.wlan.antMatrix.antenna.get(antenna = repcap.Antenna.Default) \n
		This remote control command specifies the antenna assignment of the receive path. \n
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Antenna')
			:return: receiver_antenna: ANTenna1 | ANTenna2 | ANTenna3 | ANTenna4 | ANTenna5 | ANTenna6 | ANTenna7 | ANTenna8 | ANT1 | ANT2 | ANT3 | ANT4 | ANT5 | ANT6 | ANT7 | ANT8 Antenna assignment of the receiver path"""
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		response = self._core.io.query_str(f'CONFigure:WLAN:ANTMatrix:ANTenna{antenna_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.AntennaA)

	def clone(self) -> 'Antenna':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Antenna(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
