from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Unit:
	"""Unit commands group definition. 5 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("unit", core, parent)

	@property
	def thd(self):
		"""thd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_thd'):
			from .Thd import Thd
			self._thd = Thd(self._core, self._cmd_group)
		return self._thd

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def pmeter(self):
		"""pmeter commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pmeter'):
			from .Pmeter import Pmeter
			self._pmeter = Pmeter(self._core, self._cmd_group)
		return self._pmeter

	@property
	def angle(self):
		"""angle commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_angle'):
			from .Angle import Angle
			self._angle = Angle(self._core, self._cmd_group)
		return self._angle

	def clone(self) -> 'Unit':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Unit(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
