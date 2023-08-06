from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 7 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	@property
	def burst(self):
		"""burst commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_burst'):
			from .Burst import Burst
			self._burst = Burst(self._core, self._cmd_group)
		return self._burst

	@property
	def pattern(self):
		"""pattern commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import Pattern
			self._pattern = Pattern(self._core, self._cmd_group)
		return self._pattern

	def clone(self) -> 'Current':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Current(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
