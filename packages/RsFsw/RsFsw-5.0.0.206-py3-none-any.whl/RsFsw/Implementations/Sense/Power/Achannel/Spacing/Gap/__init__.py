from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gap:
	"""Gap commands group definition. 3 total commands, 2 Subgroups, 0 group commands
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

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	@property
	def manual(self):
		"""manual commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_manual'):
			from .Manual import Manual
			self._manual = Manual(self._core, self._cmd_group)
		return self._manual

	def clone(self) -> 'Gap':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Gap(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
