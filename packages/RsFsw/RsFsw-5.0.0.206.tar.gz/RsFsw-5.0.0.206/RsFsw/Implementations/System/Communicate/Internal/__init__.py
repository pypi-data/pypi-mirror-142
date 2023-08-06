from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Internal:
	"""Internal commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("internal", core, parent)

	@property
	def completed(self):
		"""completed commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_completed'):
			from .Completed import Completed
			self._completed = Completed(self._core, self._cmd_group)
		return self._completed

	@property
	def command(self):
		"""command commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_command'):
			from .Command import Command
			self._command = Command(self._core, self._cmd_group)
		return self._command

	def clone(self) -> 'Internal':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Internal(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
