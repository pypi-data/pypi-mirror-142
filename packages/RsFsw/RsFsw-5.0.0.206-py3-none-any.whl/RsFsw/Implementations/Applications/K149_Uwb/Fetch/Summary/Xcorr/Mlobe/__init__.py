from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mlobe:
	"""Mlobe commands group definition. 16 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mlobe", core, parent)

	@property
	def minimum(self):
		"""minimum commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_minimum'):
			from .Minimum import Minimum
			self._minimum = Minimum(self._core, self._cmd_group)
		return self._minimum

	@property
	def peak(self):
		"""peak commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_peak'):
			from .Peak import Peak
			self._peak = Peak(self._core, self._cmd_group)
		return self._peak

	@property
	def width(self):
		"""width commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_width'):
			from .Width import Width
			self._width = Width(self._core, self._cmd_group)
		return self._width

	def clone(self) -> 'Mlobe':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mlobe(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
