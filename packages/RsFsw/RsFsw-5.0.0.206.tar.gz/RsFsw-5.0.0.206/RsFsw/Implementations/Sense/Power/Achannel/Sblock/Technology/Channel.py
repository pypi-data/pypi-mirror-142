from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import enums
from ....... import repcap


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

	def set(self, standard: enums.TechnologyStandardA, subBlock=repcap.SubBlock.Default, channel=repcap.Channel.Default) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:SBLock<sb>:TECHnology[:CHANnel<ch>] \n
		Snippet: driver.sense.power.achannel.sblock.technology.channel.set(standard = enums.TechnologyStandardA.GSM, subBlock = repcap.SubBlock.Default, channel = repcap.Channel.Default) \n
		This command defines the technology used for transmission by the specified MSR Tx channel. This command is for MSR
		signals only (see method RsFsw.Calculate.Marker.Function.Power.preset) . For details on MSR signals see 'Measurement on
		multi-standard radio (MSR) signals'. \n
			:param standard: Technology used for transmission GSM Transmission according to GSM standard WCDMa Transmission according to W-CDMA standard LTE_1_40 | LTE_3_00 | LTE_5_00 | LTE_10_00 | LTE_15_00 | LTE_20_00 Transmission according to LTE standard for different channel bandwidths NR5G_fr1_5 | NR5G_fr1_10 | NR5G_fr1_15 | NR5G_fr1_20 | NR5G_fr1_25 | NR5G_fr1_30 | NR5G_fr1_40 | NR5G_fr1_50 | NR5G_fr1_60 | NR5G_fr1_70 | NR5G_fr1_80 | NR5G_fr1_90 | NR5G_fr1_100 | NR5G_fr2_50 | NR5G_fr2_100 | NR5G_fr2_200 | NR5G_fr2_400 Transmission according to new radio 5G standard USER User-defined transmission; no automatic preconfiguration possible
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sblock')
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Channel')
		"""
		param = Conversions.enum_scalar_to_str(standard, enums.TechnologyStandardA)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SENSe:POWer:ACHannel:SBLock{subBlock_cmd_val}:TECHnology:CHANnel{channel_cmd_val} {param}')

	# noinspection PyTypeChecker
	def get(self, subBlock=repcap.SubBlock.Default, channel=repcap.Channel.Default) -> enums.TechnologyStandardA:
		"""SCPI: [SENSe]:POWer:ACHannel:SBLock<sb>:TECHnology[:CHANnel<ch>] \n
		Snippet: value: enums.TechnologyStandardA = driver.sense.power.achannel.sblock.technology.channel.get(subBlock = repcap.SubBlock.Default, channel = repcap.Channel.Default) \n
		This command defines the technology used for transmission by the specified MSR Tx channel. This command is for MSR
		signals only (see method RsFsw.Calculate.Marker.Function.Power.preset) . For details on MSR signals see 'Measurement on
		multi-standard radio (MSR) signals'. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Sblock')
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Channel')
			:return: standard: Technology used for transmission GSM Transmission according to GSM standard WCDMa Transmission according to W-CDMA standard LTE_1_40 | LTE_3_00 | LTE_5_00 | LTE_10_00 | LTE_15_00 | LTE_20_00 Transmission according to LTE standard for different channel bandwidths NR5G_fr1_5 | NR5G_fr1_10 | NR5G_fr1_15 | NR5G_fr1_20 | NR5G_fr1_25 | NR5G_fr1_30 | NR5G_fr1_40 | NR5G_fr1_50 | NR5G_fr1_60 | NR5G_fr1_70 | NR5G_fr1_80 | NR5G_fr1_90 | NR5G_fr1_100 | NR5G_fr2_50 | NR5G_fr2_100 | NR5G_fr2_200 | NR5G_fr2_400 Transmission according to new radio 5G standard USER User-defined transmission; no automatic preconfiguration possible"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:SBLock{subBlock_cmd_val}:TECHnology:CHANnel{channel_cmd_val}?')
		return Conversions.str_to_scalar_enum(response, enums.TechnologyStandardA)

	def clone(self) -> 'Channel':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Channel(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
