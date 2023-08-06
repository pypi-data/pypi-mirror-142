from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Paste:
	"""Paste commands group definition. 7 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("paste", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	@property
	def slot(self):
		"""slot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_slot'):
			from .Slot import Slot
			self._slot = Slot(self._core, self._cmd_group)
		return self._slot

	@property
	def to(self):
		"""to commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_to'):
			from .To import To
			self._to = To(self._core, self._cmd_group)
		return self._to

	def clone(self) -> 'Paste':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Paste(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
