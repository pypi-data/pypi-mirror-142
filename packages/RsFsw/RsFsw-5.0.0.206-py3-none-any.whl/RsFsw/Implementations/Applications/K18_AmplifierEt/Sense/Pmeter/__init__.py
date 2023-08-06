from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pmeter:
	"""Pmeter commands group definition. 18 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pmeter", core, parent)

	@property
	def level(self):
		"""level commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_level'):
			from .Level import Level
			self._level = Level(self._core, self._cmd_group)
		return self._level

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def mtime(self):
		"""mtime commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mtime'):
			from .Mtime import Mtime
			self._mtime = Mtime(self._core, self._cmd_group)
		return self._mtime

	@property
	def roffset(self):
		"""roffset commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_roffset'):
			from .Roffset import Roffset
			self._roffset = Roffset(self._core, self._cmd_group)
		return self._roffset

	@property
	def soffset(self):
		"""soffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_soffset'):
			from .Soffset import Soffset
			self._soffset = Soffset(self._core, self._cmd_group)
		return self._soffset

	@property
	def trigger(self):
		"""trigger commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	@property
	def dcycle(self):
		"""dcycle commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dcycle'):
			from .Dcycle import Dcycle
			self._dcycle = Dcycle(self._core, self._cmd_group)
		return self._dcycle

	@property
	def update(self):
		"""update commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_update'):
			from .Update import Update
			self._update = Update(self._core, self._cmd_group)
		return self._update

	def clone(self) -> 'Pmeter':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pmeter(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
