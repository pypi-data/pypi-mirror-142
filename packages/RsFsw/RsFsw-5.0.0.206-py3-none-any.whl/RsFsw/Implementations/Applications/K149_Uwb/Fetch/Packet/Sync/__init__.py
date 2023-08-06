from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sync:
	"""Sync commands group definition. 10 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sync", core, parent)

	@property
	def code(self):
		"""code commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_code'):
			from .Code import Code
			self._code = Code(self._core, self._cmd_group)
		return self._code

	@property
	def delta(self):
		"""delta commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_delta'):
			from .Delta import Delta
			self._delta = Delta(self._core, self._cmd_group)
		return self._delta

	@property
	def sfd(self):
		"""sfd commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfd'):
			from .Sfd import Sfd
			self._sfd = Sfd(self._core, self._cmd_group)
		return self._sfd

	@property
	def sync(self):
		"""sync commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sync'):
			from .Sync import Sync
			self._sync = Sync(self._core, self._cmd_group)
		return self._sync

	def clone(self) -> 'Sync':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sync(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
