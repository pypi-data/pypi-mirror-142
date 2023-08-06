from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Test:
	"""Test commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("test", core, parent)

	@property
	def redo(self):
		"""redo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_redo'):
			from .Redo import Redo
			self._redo = Redo(self._core, self._cmd_group)
		return self._redo

	@property
	def undo(self):
		"""undo commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_undo'):
			from .Undo import Undo
			self._undo = Undo(self._core, self._cmd_group)
		return self._undo

	def clone(self) -> 'Test':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Test(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
