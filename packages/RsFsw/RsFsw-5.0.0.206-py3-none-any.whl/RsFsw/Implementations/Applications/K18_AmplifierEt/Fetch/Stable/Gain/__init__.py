from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gain:
	"""Gain commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gain", core, parent)

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_average'):
			from .Average import Average
			self._average = Average(self._core, self._cmd_group)
		return self._average

	@property
	def maximum(self):
		"""maximum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maximum'):
			from .Maximum import Maximum
			self._maximum = Maximum(self._core, self._cmd_group)
		return self._maximum

	@property
	def minimum(self):
		"""minimum commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_minimum'):
			from .Minimum import Minimum
			self._minimum = Minimum(self._core, self._cmd_group)
		return self._minimum

	@property
	def stDeviation(self):
		"""stDeviation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stDeviation'):
			from .StDeviation import StDeviation
			self._stDeviation = StDeviation(self._core, self._cmd_group)
		return self._stDeviation

	@property
	def selected(self):
		"""selected commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_selected'):
			from .Selected import Selected
			self._selected = Selected(self._core, self._cmd_group)
		return self._selected

	def clone(self) -> 'Gain':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Gain(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
