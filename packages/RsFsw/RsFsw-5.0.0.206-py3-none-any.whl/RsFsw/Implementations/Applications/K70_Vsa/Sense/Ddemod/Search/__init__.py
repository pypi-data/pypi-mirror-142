from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Search:
	"""Search commands group definition. 36 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("search", core, parent)

	@property
	def burst(self):
		"""burst commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_burst'):
			from .Burst import Burst
			self._burst = Burst(self._core, self._cmd_group)
		return self._burst

	@property
	def mburst(self):
		"""mburst commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_mburst'):
			from .Mburst import Mburst
			self._mburst = Mburst(self._core, self._cmd_group)
		return self._mburst

	@property
	def sync(self):
		"""sync commands group. 14 Sub-classes, 2 commands."""
		if not hasattr(self, '_sync'):
			from .Sync import Sync
			self._sync = Sync(self._core, self._cmd_group)
		return self._sync

	@property
	def pattern(self):
		"""pattern commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import Pattern
			self._pattern = Pattern(self._core, self._cmd_group)
		return self._pattern

	@property
	def pulse(self):
		"""pulse commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pulse'):
			from .Pulse import Pulse
			self._pulse = Pulse(self._core, self._cmd_group)
		return self._pulse

	@property
	def time(self):
		"""time commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_time'):
			from .Time import Time
			self._time = Time(self._core, self._cmd_group)
		return self._time

	def clone(self) -> 'Search':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Search(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
