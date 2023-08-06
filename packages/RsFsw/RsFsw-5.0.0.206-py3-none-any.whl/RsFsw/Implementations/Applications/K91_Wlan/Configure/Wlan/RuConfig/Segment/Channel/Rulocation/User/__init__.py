from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal.RepeatedCapability import RepeatedCapability
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class User:
	"""User commands group definition. 8 total commands, 7 Subgroups, 1 group commands
	Repeated Capability: UserIx, default value after init: UserIx.Ix1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("user", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_userIx_get', 'repcap_userIx_set', repcap.UserIx.Ix1)

	def repcap_userIx_set(self, userIx: repcap.UserIx) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to UserIx.Default
		Default value after init: UserIx.Ix1"""
		self._cmd_group.set_repcap_enum_value(userIx)

	def repcap_userIx_get(self) -> repcap.UserIx:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def insert(self):
		"""insert commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_insert'):
			from .Insert import Insert
			self._insert = Insert(self._core, self._cmd_group)
		return self._insert

	@property
	def mcsIndex(self):
		"""mcsIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcsIndex'):
			from .McsIndex import McsIndex
			self._mcsIndex = McsIndex(self._core, self._cmd_group)
		return self._mcsIndex

	@property
	def nsts(self):
		"""nsts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nsts'):
			from .Nsts import Nsts
			self._nsts = Nsts(self._core, self._cmd_group)
		return self._nsts

	@property
	def tbeamforming(self):
		"""tbeamforming commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tbeamforming'):
			from .Tbeamforming import Tbeamforming
			self._tbeamforming = Tbeamforming(self._core, self._cmd_group)
		return self._tbeamforming

	@property
	def dcm(self):
		"""dcm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dcm'):
			from .Dcm import Dcm
			self._dcm = Dcm(self._core, self._cmd_group)
		return self._dcm

	@property
	def coding(self):
		"""coding commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_coding'):
			from .Coding import Coding
			self._coding = Coding(self._core, self._cmd_group)
		return self._coding

	@property
	def count(self):
		"""count commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Count import Count
			self._count = Count(self._core, self._cmd_group)
		return self._count

	def delete(self, segment=repcap.Segment.Default, channel=repcap.Channel.Default, ruAllocationIx=repcap.RuAllocationIx.Default, userIx=repcap.UserIx.Default) -> None:
		"""SCPI: CONFigure:WLAN:RUConfig:SEGMent<seg>:CHANnel<ch>:RULocation<cf>:USER<mu>:DELete \n
		Snippet: driver.applications.k91Wlan.configure.wlan.ruConfig.segment.channel.rulocation.user.delete(segment = repcap.Segment.Default, channel = repcap.Channel.Default, ruAllocationIx = repcap.RuAllocationIx.Default, userIx = repcap.UserIx.Default) \n
		Deletes the selected user (station) from the HE Multi-User Downlink PPDU configuration table (for MIMO configuration
		only) . \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Channel')
			:param ruAllocationIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rulocation')
			:param userIx: optional repeated capability selector. Default value: Ix1 (settable in the interface 'User')
		"""
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		ruAllocationIx_cmd_val = self._cmd_group.get_repcap_cmd_value(ruAllocationIx, repcap.RuAllocationIx)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		self._core.io.write(f'CONFigure:WLAN:RUConfig:SEGMent{segment_cmd_val}:CHANnel{channel_cmd_val}:RULocation{ruAllocationIx_cmd_val}:USER{userIx_cmd_val}:DELete')

	def delete_with_opc(self, segment=repcap.Segment.Default, channel=repcap.Channel.Default, ruAllocationIx=repcap.RuAllocationIx.Default, userIx=repcap.UserIx.Default, opc_timeout_ms: int = -1) -> None:
		segment_cmd_val = self._cmd_group.get_repcap_cmd_value(segment, repcap.Segment)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		ruAllocationIx_cmd_val = self._cmd_group.get_repcap_cmd_value(ruAllocationIx, repcap.RuAllocationIx)
		userIx_cmd_val = self._cmd_group.get_repcap_cmd_value(userIx, repcap.UserIx)
		"""SCPI: CONFigure:WLAN:RUConfig:SEGMent<seg>:CHANnel<ch>:RULocation<cf>:USER<mu>:DELete \n
		Snippet: driver.applications.k91Wlan.configure.wlan.ruConfig.segment.channel.rulocation.user.delete_with_opc(segment = repcap.Segment.Default, channel = repcap.Channel.Default, ruAllocationIx = repcap.RuAllocationIx.Default, userIx = repcap.UserIx.Default) \n
		Deletes the selected user (station) from the HE Multi-User Downlink PPDU configuration table (for MIMO configuration
		only) . \n
		Same as delete, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param segment: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Segment')
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Channel')
			:param ruAllocationIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Rulocation')
			:param userIx: optional repeated capability selector. Default value: Ix1 (settable in the interface 'User')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:WLAN:RUConfig:SEGMent{segment_cmd_val}:CHANnel{channel_cmd_val}:RULocation{ruAllocationIx_cmd_val}:USER{userIx_cmd_val}:DELete', opc_timeout_ms)

	def clone(self) -> 'User':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = User(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
