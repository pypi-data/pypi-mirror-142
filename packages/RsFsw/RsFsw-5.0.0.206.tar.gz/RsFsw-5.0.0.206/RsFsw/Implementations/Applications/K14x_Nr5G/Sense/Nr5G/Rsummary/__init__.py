from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rsummary:
	"""Rsummary commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rsummary", core, parent)

	@property
	def ccResult(self):
		"""ccResult commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ccResult'):
			from .CcResult import CcResult
			self._ccResult = CcResult(self._core, self._cmd_group)
		return self._ccResult

	@property
	def pmode(self):
		"""pmode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmode'):
			from .Pmode import Pmode
			self._pmode = Pmode(self._core, self._cmd_group)
		return self._pmode

	@property
	def show(self):
		"""show commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_show'):
			from .Show import Show
			self._show = Show(self._core, self._cmd_group)
		return self._show

	def clone(self) -> 'Rsummary':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rsummary(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
