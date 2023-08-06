from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ualternate:
	"""Ualternate commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: UpperAltChannel, default value after init: UpperAltChannel.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ualternate", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_upperAltChannel_get', 'repcap_upperAltChannel_set', repcap.UpperAltChannel.Nr1)

	def repcap_upperAltChannel_set(self, upperAltChannel: repcap.UpperAltChannel) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to UpperAltChannel.Default
		Default value after init: UpperAltChannel.Nr1"""
		self._cmd_group.set_repcap_enum_value(upperAltChannel)

	def repcap_upperAltChannel_get(self) -> repcap.UpperAltChannel:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, alpha: float, upperAltChannel=repcap.UpperAltChannel.Default) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:FILTer:ALPHa:UALTernate<ch> \n
		Snippet: driver.sense.power.achannel.filterPy.alpha.ualternate.set(alpha = 1.0, upperAltChannel = repcap.UpperAltChannel.Default) \n
		This command defines the roll-off factor for the upper alternate channels' weighting filter for asymmetrical MSR signals.
		To configure the factor for the upper alternate channels, use the [SENSe:]POWer:ACHannel:FILTer:ALPHa:ALTernate<ch>
		command. \n
			:param alpha: Roll-off factor Range: 0 to 1
			:param upperAltChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ualternate')
		"""
		param = Conversions.decimal_value_to_str(alpha)
		upperAltChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(upperAltChannel, repcap.UpperAltChannel)
		self._core.io.write(f'SENSe:POWer:ACHannel:FILTer:ALPHa:UALTernate{upperAltChannel_cmd_val} {param}')

	def get(self, upperAltChannel=repcap.UpperAltChannel.Default) -> float:
		"""SCPI: [SENSe]:POWer:ACHannel:FILTer:ALPHa:UALTernate<ch> \n
		Snippet: value: float = driver.sense.power.achannel.filterPy.alpha.ualternate.get(upperAltChannel = repcap.UpperAltChannel.Default) \n
		This command defines the roll-off factor for the upper alternate channels' weighting filter for asymmetrical MSR signals.
		To configure the factor for the upper alternate channels, use the [SENSe:]POWer:ACHannel:FILTer:ALPHa:ALTernate<ch>
		command. \n
			:param upperAltChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ualternate')
			:return: alpha: Roll-off factor Range: 0 to 1"""
		upperAltChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(upperAltChannel, repcap.UpperAltChannel)
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:FILTer:ALPHa:UALTernate{upperAltChannel_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Ualternate':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ualternate(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
