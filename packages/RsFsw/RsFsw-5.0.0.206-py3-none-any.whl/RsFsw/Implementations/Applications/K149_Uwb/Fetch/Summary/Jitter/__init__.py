from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Jitter:
	"""Jitter commands group definition. 8 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("jitter", core, parent)

	@property
	def chip(self):
		"""chip commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_chip'):
			from .Chip import Chip
			self._chip = Chip(self._core, self._cmd_group)
		return self._chip

	@property
	def symbol(self):
		"""symbol commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbol'):
			from .Symbol import Symbol
			self._symbol = Symbol(self._core, self._cmd_group)
		return self._symbol

	def clone(self) -> 'Jitter':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Jitter(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
