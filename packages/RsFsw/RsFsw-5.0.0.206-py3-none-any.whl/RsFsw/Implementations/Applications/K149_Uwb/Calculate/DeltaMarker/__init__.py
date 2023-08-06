from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DeltaMarker:
	"""DeltaMarker commands group definition. 1 total commands, 1 Subgroups, 0 group commands
	Repeated Capability: DeltaMarker, default value after init: DeltaMarker.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("deltaMarker", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_deltaMarker_get', 'repcap_deltaMarker_set', repcap.DeltaMarker.Nr1)

	def repcap_deltaMarker_set(self, deltaMarker: repcap.DeltaMarker) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to DeltaMarker.Default
		Default value after init: DeltaMarker.Nr1"""
		self._cmd_group.set_repcap_enum_value(deltaMarker)

	def repcap_deltaMarker_get(self) -> repcap.DeltaMarker:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def function(self):
		"""function commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_function'):
			from .Function import Function
			self._function = Function(self._core, self._cmd_group)
		return self._function

	def clone(self) -> 'DeltaMarker':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DeltaMarker(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
