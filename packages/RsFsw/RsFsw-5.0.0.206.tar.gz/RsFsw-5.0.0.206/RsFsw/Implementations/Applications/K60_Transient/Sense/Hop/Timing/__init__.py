from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Timing:
	"""Timing commands group definition. 15 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("timing", core, parent)

	@property
	def begin(self):
		"""begin commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_begin'):
			from .Begin import Begin
			self._begin = Begin(self._core, self._cmd_group)
		return self._begin

	@property
	def dwell(self):
		"""dwell commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_dwell'):
			from .Dwell import Dwell
			self._dwell = Dwell(self._core, self._cmd_group)
		return self._dwell

	@property
	def switching(self):
		"""switching commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_switching'):
			from .Switching import Switching
			self._switching = Switching(self._core, self._cmd_group)
		return self._switching

	def clone(self) -> 'Timing':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Timing(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
