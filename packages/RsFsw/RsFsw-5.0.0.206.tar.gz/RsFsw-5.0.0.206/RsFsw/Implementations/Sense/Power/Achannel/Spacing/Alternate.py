from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
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

	def set(self, spacing: float, channel=repcap.Channel.Default) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:SPACing:ALTernate<ch> \n
		Snippet: driver.sense.power.achannel.spacing.alternate.set(spacing = 1.0, channel = repcap.Channel.Default) \n
		This command defines the distance from transmission channel to alternate channels. For MSR signals, this command defines
		the distance from the CF of the first Tx channel in the first sub block to the lower alternate channel. To configure the
		spacing for the upper alternate channel in asymmetrical configurations,
		use the [SENSe:]POWer:ACHannel:SPACing:UALTernate<ch> command. If you set the channel spacing for the first alternate
		channel, the R&S FSW adjusts the spacing of alternate channels of a lower order, but not the other way round (not for MSR
		signals) . The command works hierarchically: to set a distance from the transmission channel to the 2nd and 3rd alternate
		channel, you have to define a spacing for the 2nd alternate channel first. \n
			:param spacing: Range: 100 Hz to 2000 MHz, Unit: Hz
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Alternate')
		"""
		param = Conversions.decimal_value_to_str(spacing)
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		self._core.io.write(f'SENSe:POWer:ACHannel:SPACing:ALTernate{channel_cmd_val} {param}')

	def get(self, channel=repcap.Channel.Default) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:SPACing:ALTernate<ch> \n
		Snippet: value: float = driver.sense.power.achannel.spacing.alternate.get(channel = repcap.Channel.Default) \n
		This command defines the distance from transmission channel to alternate channels. For MSR signals, this command defines
		the distance from the CF of the first Tx channel in the first sub block to the lower alternate channel. To configure the
		spacing for the upper alternate channel in asymmetrical configurations,
		use the [SENSe:]POWer:ACHannel:SPACing:UALTernate<ch> command. If you set the channel spacing for the first alternate
		channel, the R&S FSW adjusts the spacing of alternate channels of a lower order, but not the other way round (not for MSR
		signals) . The command works hierarchically: to set a distance from the transmission channel to the 2nd and 3rd alternate
		channel, you have to define a spacing for the 2nd alternate channel first. \n
			:param channel: optional repeated capability selector. Default value: Ch1 (settable in the interface 'Alternate')
			:return: spacing: Range: 100 Hz to 2000 MHz, Unit: Hz"""
		channel_cmd_val = self._cmd_group.get_repcap_cmd_value(channel, repcap.Channel)
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:SPACing:ALTernate{channel_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Alternate':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Alternate(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
