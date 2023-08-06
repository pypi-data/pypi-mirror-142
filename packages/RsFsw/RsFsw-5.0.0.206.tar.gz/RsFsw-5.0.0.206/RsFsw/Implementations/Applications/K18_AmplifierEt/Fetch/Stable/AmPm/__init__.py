from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AmPm:
	"""AmPm commands group definition. 5 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("amPm", core, parent)

	@property
	def cwidth(self):
		"""cwidth commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_cwidth'):
			from .Cwidth import Cwidth
			self._cwidth = Cwidth(self._core, self._cmd_group)
		return self._cwidth

	def clone(self) -> 'AmPm':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AmPm(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
