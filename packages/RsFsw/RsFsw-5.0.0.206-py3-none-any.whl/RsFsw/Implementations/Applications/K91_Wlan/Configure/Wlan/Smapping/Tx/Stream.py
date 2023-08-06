from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Types import DataType
from ........Internal.StructBase import StructBase
from ........Internal.ArgStruct import ArgStruct
from ........Internal.ArgSingleList import ArgSingleList
from ........Internal.ArgSingle import ArgSingle
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stream:
	"""Stream commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Antenna, default value after init: Antenna.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stream", core, parent)
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

	def set(self, stsi: float, stsq: float, channel=repcap.Channel.Default, antenna=repcap.Antenna.Default) -> None:
		"""SCPI: CONFigure:WLAN:SMAPping:TX<ch>:STReam<ant> \n
		Snippet: driver.applications.k91Wlan.configure.wlan.smapping.tx.stream.set(stsi = 1.0, stsq = 1.0, channel = repcap.Channel.Default, antenna = repcap.Antenna.Default) \n
		This remote control command specifies the mapping for a specific stream and antenna. \n
			:param stsi: Imag part of the complex element of the STS-Stream
			:param stsq: Real part of the complex element of the STS-Stream
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Tx')
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('stsi', stsi, DataType.Float), ArgSingle('stsq', stsq, DataType.Float))
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		self._core.io.write(f'CONFigure:WLAN:SMAPping:TX{channel_cmd_val}:STReam{antenna_cmd_val} {param}'.rstrip())

	# noinspection PyTypeChecker
	class StreamStruct(StructBase):
		"""Response structure. Fields: \n
			- Stsi: float: Imag part of the complex element of the STS-Stream
			- Stsq: float: Real part of the complex element of the STS-Stream"""
		__meta_args_list = [
			ArgStruct.scalar_float('Stsi'),
			ArgStruct.scalar_float('Stsq')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Stsi: float = None
			self.Stsq: float = None

	def get(self, channel=repcap.Channel.Default, antenna=repcap.Antenna.Default) -> StreamStruct:
		"""SCPI: CONFigure:WLAN:SMAPping:TX<ch>:STReam<ant> \n
		Snippet: value: StreamStruct = driver.applications.k91Wlan.configure.wlan.smapping.tx.stream.get(channel = repcap.Channel.Default, antenna = repcap.Antenna.Default) \n
		This remote control command specifies the mapping for a specific stream and antenna. \n
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Tx')
			:param antenna: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Stream')
			:return: structure: for return value, see the help for StreamStruct structure arguments."""
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		antenna_cmd_val = self._cmd_group.get_repcap_cmd_value(antenna, repcap.Antenna)
		return self._core.io.query_struct(f'CONFigure:WLAN:SMAPping:TX{channel_cmd_val}:STReam{antenna_cmd_val}?', self.__class__.StreamStruct())

	def clone(self) -> 'Stream':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Stream(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
