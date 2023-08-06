from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RiseTopPoint:
	"""RiseTopPoint commands group definition. 14 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("riseTopPoint", core, parent)

	@property
	def time(self):
		"""time commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_time'):
			from .Time import Time
			self._time = Time(self._core, self._cmd_group)
		return self._time

	@property
	def level(self):
		"""level commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_level'):
			from .Level import Level
			self._level = Level(self._core, self._cmd_group)
		return self._level

	def clone(self) -> 'RiseTopPoint':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RiseTopPoint(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
