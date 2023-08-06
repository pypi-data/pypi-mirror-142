from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Factor:
	"""Factor commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("factor", core, parent)

	@property
	def numerator(self):
		"""numerator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_numerator'):
			from .Numerator import Numerator
			self._numerator = Numerator(self._core, self._cmd_group)
		return self._numerator

	@property
	def denominator(self):
		"""denominator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_denominator'):
			from .Denominator import Denominator
			self._denominator = Denominator(self._core, self._cmd_group)
		return self._denominator

	def clone(self) -> 'Factor':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Factor(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
