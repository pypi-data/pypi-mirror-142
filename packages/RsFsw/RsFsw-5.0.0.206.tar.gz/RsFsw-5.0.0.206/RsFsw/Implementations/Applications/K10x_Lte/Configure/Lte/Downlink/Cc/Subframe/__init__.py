from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Subframe:
	"""Subframe commands group definition. 14 total commands, 2 Subgroups, 0 group commands
	Repeated Capability: Subframe, default value after init: Subframe.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("subframe", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_subframe_get', 'repcap_subframe_set', repcap.Subframe.Nr0)

	def repcap_subframe_set(self, subframe: repcap.Subframe) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Subframe.Default
		Default value after init: Subframe.Nr0"""
		self._cmd_group.set_repcap_enum_value(subframe)

	def repcap_subframe_get(self) -> repcap.Subframe:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def alCount(self):
		"""alCount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_alCount'):
			from .AlCount import AlCount
			self._alCount = AlCount(self._core, self._cmd_group)
		return self._alCount

	@property
	def alloc(self):
		"""alloc commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_alloc'):
			from .Alloc import Alloc
			self._alloc = Alloc(self._core, self._cmd_group)
		return self._alloc

	def clone(self) -> 'Subframe':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Subframe(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
