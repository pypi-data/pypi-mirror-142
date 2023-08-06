from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........Internal.Utilities import trim_str_response
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gap:
	"""Gap commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: GapChannel, default value after init: GapChannel.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gap", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_gapChannel_get', 'repcap_gapChannel_set', repcap.GapChannel.Nr1)

	def repcap_gapChannel_set(self, gapChannel: repcap.GapChannel) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to GapChannel.Default
		Default value after init: GapChannel.Nr1"""
		self._cmd_group.set_repcap_enum_value(gapChannel)

	def repcap_gapChannel_get(self) -> repcap.GapChannel:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, name: str, gapChannel=repcap.GapChannel.Default) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:NAME:GAP<gap> \n
		Snippet: driver.applications.k14Xnr5G.sense.power.achannel.name.gap.set(name = '1', gapChannel = repcap.GapChannel.Default) \n
		No command help available \n
			:param name: No help available
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
		"""
		param = Conversions.value_to_quoted_str(name)
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		self._core.io.write(f'SENSe:POWer:ACHannel:NAME:GAP{gapChannel_cmd_val} {param}')

	def get(self, gapChannel=repcap.GapChannel.Default) -> str:
		"""SCPI: [SENSe]:POWer:ACHannel:NAME:GAP<gap> \n
		Snippet: value: str = driver.applications.k14Xnr5G.sense.power.achannel.name.gap.get(gapChannel = repcap.GapChannel.Default) \n
		No command help available \n
			:param gapChannel: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Gap')
			:return: name: No help available"""
		gapChannel_cmd_val = self._cmd_group.get_repcap_cmd_value(gapChannel, repcap.GapChannel)
		response = self._core.io.query_str(f'SENSe:POWer:ACHannel:NAME:GAP{gapChannel_cmd_val}?')
		return trim_str_response(response)

	def clone(self) -> 'Gap':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Gap(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
