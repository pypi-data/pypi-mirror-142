from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Alternate:
	"""Alternate commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Channel, default value after init: Channel.Ch1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alternate", core, parent)
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

	def set(self, name: str, channel=repcap.Channel.Default) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:NAME:ALTernate<ch> \n
		Snippet: driver.sense.power.achannel.name.alternate.set(name = '1', channel = repcap.Channel.Default) \n
		This command defines a name for an alternate channel. For MSR ACLR measurements, this command defines the name for the
		lower alternate channel in asymmetric channel definitions. To define the name for the upper alternate channels use the
		[SENSe:]POWer:ACHannel:NAME:UALTernate<ch> command. For details on MSR signals see 'Measurement on multi-standard radio
		(MSR) signals'. \n
			:param name: String containing the name of the channel
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Alternate')
		"""
		param = Conversions.value_to_quoted_str(name)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SENSe:POWer:ACHannel:NAME:ALTernate{channel_cmd_val} {param}')

	def get(self, channel=repcap.Channel.Default) -> str:
		"""SCPI: [SENSe]:POWer:ACHannel:NAME:ALTernate<ch> \n
		Snippet: value: str = driver.sense.power.achannel.name.alternate.get(channel = repcap.Channel.Default) \n
		This command defines a name for an alternate channel. For MSR ACLR measurements, this command defines the name for the
		lower alternate channel in asymmetric channel definitions. To define the name for the upper alternate channels use the
		[SENSe:]POWer:ACHannel:NAME:UALTernate<ch> command. For details on MSR signals see 'Measurement on multi-standard radio
		(MSR) signals'. \n
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Alternate')
			:return: name: String containing the name of the channel"""
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:NAME:ALTernate{channel_cmd_val}?')
		return trim_str_response(response)

	def clone(self) -> 'Alternate':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Alternate(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
