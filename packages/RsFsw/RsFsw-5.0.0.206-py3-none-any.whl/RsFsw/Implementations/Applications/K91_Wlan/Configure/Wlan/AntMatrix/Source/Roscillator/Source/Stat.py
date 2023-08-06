from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from ..........Internal.RepeatedCapability import RepeatedCapability
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stat:
	"""Stat commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Antenna, default value after init: Antenna.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stat", core, parent)
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

	def set(self, state: bool, antenna=repcap.Antenna.Default) -> None:
		"""SCPI: CONFigure:WLAN:ANTMatrix:SOURce:ROSCillator:SOURce:STAT<ant> \n
		Snippet: driver.applications.k91Wlan.configure.wlan.antMatrix.source.roscillator.source.stat.set(state = False, antenna = repcap.Antenna.Default) \n
		Queries the connection state of the external reference for each channel (see also method RsFsw.Applications.K91_Wlan.
		Configure.Wlan.AntMatrix.Source.Roscillator.Source.set) . If the IP address of the antenna is not available or valid, or
		the selected antenna is not active, an error message is returned. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 External reference not available ON | 1 External reference available
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stat')
		"""
		param = Conversions.bool_to_str(state)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		self._core.io.write(f'CONFigure:WLAN:ANTMatrix:SOURce:ROSCillator:SOURce:STAT{antenna_cmd_val} {param}')

	def get(self, antenna=repcap.Antenna.Default) -> bool:
		"""SCPI: CONFigure:WLAN:ANTMatrix:SOURce:ROSCillator:SOURce:STAT<ant> \n
		Snippet: value: bool = driver.applications.k91Wlan.configure.wlan.antMatrix.source.roscillator.source.stat.get(antenna = repcap.Antenna.Default) \n
		Queries the connection state of the external reference for each channel (see also method RsFsw.Applications.K91_Wlan.
		Configure.Wlan.AntMatrix.Source.Roscillator.Source.set) . If the IP address of the antenna is not available or valid, or
		the selected antenna is not active, an error message is returned. \n
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stat')
			:return: state: ON | OFF | 0 | 1 OFF | 0 External reference not available ON | 1 External reference available"""
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		response = self._core.io.query_str(f'CONFigure:WLAN:ANTMatrix:SOURce:ROSCillator:SOURce:STAT{antenna_cmd_val}?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Stat':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Stat(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
