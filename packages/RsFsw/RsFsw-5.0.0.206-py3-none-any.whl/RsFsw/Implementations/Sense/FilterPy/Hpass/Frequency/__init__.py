from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	@property
	def absolute(self):
		"""absolute commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_absolute'):
			from .Absolute import Absolute
			self._absolute = Absolute(self._core, self._cmd_group)
		return self._absolute

	@property
	def manual(self):
		"""manual commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_manual'):
			from .Manual import Manual
			self._manual = Manual(self._core, self._cmd_group)
		return self._manual

	def clone(self) -> 'Frequency':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Frequency(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
