from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	@property
	def begin(self):
		"""begin commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_begin'):
			from .Begin import Begin
			self._begin = Begin(self._core, self._cmd_group)
		return self._begin

	@property
	def end(self):
		"""end commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_end'):
			from .End import End
			self._end = End(self._core, self._cmd_group)
		return self._end

	def clone(self) -> 'Offset':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Offset(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
