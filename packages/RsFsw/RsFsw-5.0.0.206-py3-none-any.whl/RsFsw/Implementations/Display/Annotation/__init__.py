from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Annotation:
	"""Annotation commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("annotation", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def cbar(self):
		"""cbar commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbar'):
			from .Cbar import Cbar
			self._cbar = Cbar(self._core, self._cmd_group)
		return self._cbar

	def clone(self) -> 'Annotation':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Annotation(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
