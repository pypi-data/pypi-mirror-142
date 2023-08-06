from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Channel:
	"""Channel commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Channel, default value after init: Channel.Ch1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("channel", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_channel_get', 'repcap_channel_set', repcap.Channel.Ch1)

	def repcap_channel_set(self, channel: repcap.Channel) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Channel.Default
		Default value after init: Channel.Ch1"""
		self._cmd_group.set_repcap_enum_value(channel)

	def repcap_channel_get(self) -> repcap.Channel:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, frequency: float, subBlock=repcap.SubBlock.Default, channel=repcap.Channel.Default) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:SBLock<sb>:CENTer[:CHANnel<ch>] \n
		Snippet: driver.applications.k14Xnr5G.sense.power.achannel.sblock.center.channel.set(frequency = 1.0, subBlock = repcap.SubBlock.Default, channel = repcap.Channel.Default) \n
		No command help available \n
			:param frequency: No help available
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sblock')
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Channel')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SENSe:POWer:ACHannel:SBLock{subBlock_cmd_val}:CENTer:CHANnel{channel_cmd_val} {param}')

	def get(self, subBlock=repcap.SubBlock.Default, channel=repcap.Channel.Default) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:SBLock<sb>:CENTer[:CHANnel<ch>] \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.power.achannel.sblock.center.channel.get(subBlock = repcap.SubBlock.Default, channel = repcap.Channel.Default) \n
		No command help available \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sblock')
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Channel')
			:return: frequency: No help available"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:SBLock{subBlock_cmd_val}:CENTer:CHANnel{channel_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Channel':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Channel(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
