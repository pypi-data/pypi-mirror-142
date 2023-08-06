from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sem:
	"""Sem commands group definition. 5 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sem", core, parent)

	@property
	def amPower(self):
		"""amPower commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_amPower'):
			from .AmPower import AmPower
			self._amPower = AmPower(self._core, self._cmd_group)
		return self._amPower

	@property
	def iff(self):
		"""iff commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iff'):
			from .Iff import Iff
			self._iff = Iff(self._core, self._cmd_group)
		return self._iff

	@property
	def ntab(self):
		"""ntab commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ntab'):
			from .Ntab import Ntab
			self._ntab = Ntab(self._core, self._cmd_group)
		return self._ntab

	@property
	def ntxu(self):
		"""ntxu commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ntxu'):
			from .Ntxu import Ntxu
			self._ntxu = Ntxu(self._core, self._cmd_group)
		return self._ntxu

	def clone(self) -> 'Sem':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sem(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
