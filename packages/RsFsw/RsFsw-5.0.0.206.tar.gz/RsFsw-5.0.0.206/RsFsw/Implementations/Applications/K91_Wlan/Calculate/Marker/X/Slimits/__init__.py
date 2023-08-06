from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Slimits:
	"""Slimits commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("slimits", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def left(self):
		"""left commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_left'):
			from .Left import Left
			self._left = Left(self._core, self._cmd_group)
		return self._left

	@property
	def right(self):
		"""right commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_right'):
			from .Right import Right
			self._right = Right(self._core, self._cmd_group)
		return self._right

	def clone(self) -> 'Slimits':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Slimits(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
