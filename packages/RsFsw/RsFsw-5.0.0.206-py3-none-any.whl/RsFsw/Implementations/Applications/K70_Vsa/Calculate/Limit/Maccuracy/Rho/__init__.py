from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rho:
	"""Rho commands group definition. 9 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rho", core, parent)

	@property
	def current(self):
		"""current commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_current'):
			from .Current import Current
			self._current = Current(self._core, self._cmd_group)
		return self._current

	@property
	def mean(self):
		"""mean commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_mean'):
			from .Mean import Mean
			self._mean = Mean(self._core, self._cmd_group)
		return self._mean

	@property
	def peak(self):
		"""peak commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_peak'):
			from .Peak import Peak
			self._peak = Peak(self._core, self._cmd_group)
		return self._peak

	def clone(self) -> 'Rho':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rho(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
