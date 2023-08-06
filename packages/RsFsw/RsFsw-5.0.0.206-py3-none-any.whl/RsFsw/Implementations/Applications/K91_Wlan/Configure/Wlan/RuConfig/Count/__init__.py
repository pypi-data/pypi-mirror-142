from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	@property
	def highest(self):
		"""highest commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_highest'):
			from .Highest import Highest
			self._highest = Highest(self._core, self._cmd_group)
		return self._highest

	@property
	def active(self):
		"""active commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_active'):
			from .Active import Active
			self._active = Active(self._core, self._cmd_group)
		return self._active

	def clone(self) -> 'Count':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Count(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
