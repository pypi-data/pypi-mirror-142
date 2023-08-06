from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Overshoot:
	"""Overshoot commands group definition. 14 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("overshoot", core, parent)

	@property
	def percent(self):
		"""percent commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_percent'):
			from .Percent import Percent
			self._percent = Percent(self._core, self._cmd_group)
		return self._percent

	@property
	def db(self):
		"""db commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_db'):
			from .Db import Db
			self._db = Db(self._core, self._cmd_group)
		return self._db

	def clone(self) -> 'Overshoot':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Overshoot(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
