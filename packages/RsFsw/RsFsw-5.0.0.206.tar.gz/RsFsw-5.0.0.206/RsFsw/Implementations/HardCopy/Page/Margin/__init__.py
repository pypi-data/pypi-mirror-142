from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Margin:
	"""Margin commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("margin", core, parent)

	@property
	def bottom(self):
		"""bottom commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bottom'):
			from .Bottom import Bottom
			self._bottom = Bottom(self._core, self._cmd_group)
		return self._bottom

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

	@property
	def top(self):
		"""top commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_top'):
			from .Top import Top
			self._top = Top(self._core, self._cmd_group)
		return self._top

	@property
	def unit(self):
		"""unit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_unit'):
			from .Unit import Unit
			self._unit = Unit(self._core, self._cmd_group)
		return self._unit

	def clone(self) -> 'Margin':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Margin(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
