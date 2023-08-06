from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mask:
	"""Mask commands group definition. 4 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mask", core, parent)

	@property
	def passed(self):
		"""passed commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_passed'):
			from .Passed import Passed
			self._passed = Passed(self._core, self._cmd_group)
		return self._passed

	def clone(self) -> 'Mask':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mask(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
