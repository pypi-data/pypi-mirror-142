from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maximum:
	"""Maximum commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	@property
	def apeak(self):
		"""apeak commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apeak'):
			from .Apeak import Apeak
			self._apeak = Apeak(self._core, self._cmd_group)
		return self._apeak

	@property
	def peak(self):
		"""peak commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_peak'):
			from .Peak import Peak
			self._peak = Peak(self._core, self._cmd_group)
		return self._peak

	@property
	def next(self):
		"""next commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_next'):
			from .Next import Next
			self._next = Next(self._core, self._cmd_group)
		return self._next

	@property
	def right(self):
		"""right commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_right'):
			from .Right import Right
			self._right = Right(self._core, self._cmd_group)
		return self._right

	@property
	def left(self):
		"""left commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_left'):
			from .Left import Left
			self._left = Left(self._core, self._cmd_group)
		return self._left

	def clone(self) -> 'Maximum':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Maximum(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
