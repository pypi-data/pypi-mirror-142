from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


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

	def set(self, name: str, upperAltChannel=repcap.UpperAltChannel.Default) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:NAME:UALTernate<ch> \n
		Snippet: driver.sense.power.achannel.name.ualternate.set(name = '1', upperAltChannel = repcap.UpperAltChannel.Default) \n
		This command defines the name for the specified upper alternate channel in asymmetrical MSR channel definitions.
		To define the name for the lower adjacent channels use the [SENSe:]POWer:ACHannel:NAME:ALTernate<ch> command. For details
		on MSR signals see 'Measurement on multi-standard radio (MSR) signals'. \n
			:param name: String containing the name of the channel
			:param upperAltChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ualternate')
		"""
		param = Conversions.value_to_quoted_str(name)
		upperAltChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(upperAltChannel, repcap.UpperAltChannel)
		self._core.io.write(f'SENSe:POWer:ACHannel:NAME:UALTernate{upperAltChannel_cmd_val} {param}')

	def get(self, upperAltChannel=repcap.UpperAltChannel.Default) -> str:
		"""SCPI: [SENSe]:POWer:ACHannel:NAME:UALTernate<ch> \n
		Snippet: value: str = driver.sense.power.achannel.name.ualternate.get(upperAltChannel = repcap.UpperAltChannel.Default) \n
		This command defines the name for the specified upper alternate channel in asymmetrical MSR channel definitions.
		To define the name for the lower adjacent channels use the [SENSe:]POWer:ACHannel:NAME:ALTernate<ch> command. For details
		on MSR signals see 'Measurement on multi-standard radio (MSR) signals'. \n
			:param upperAltChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Ualternate')
			:return: name: String containing the name of the channel"""
		upperAltChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(upperAltChannel, repcap.UpperAltChannel)
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:NAME:UALTernate{upperAltChannel_cmd_val}?')
		return trim_str_response(response)

	def clone(self) -> 'Ualternate':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ualternate(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
