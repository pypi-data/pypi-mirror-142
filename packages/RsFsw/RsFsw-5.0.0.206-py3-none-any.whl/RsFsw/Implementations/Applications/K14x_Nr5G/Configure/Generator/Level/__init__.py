from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Level:
	"""Level commands group definition. 3 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	@property
	def dutGain(self):
		"""dutGain commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dutGain'):
			from .DutGain import DutGain
			self._dutGain = DutGain(self._core, self._cmd_group)
		return self._dutGain

	@property
	def dutLimit(self):
		"""dutLimit commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_dutLimit'):
			from .DutLimit import DutLimit
			self._dutLimit = DutLimit(self._core, self._cmd_group)
		return self._dutLimit

	def clone(self) -> 'Level':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Level(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
