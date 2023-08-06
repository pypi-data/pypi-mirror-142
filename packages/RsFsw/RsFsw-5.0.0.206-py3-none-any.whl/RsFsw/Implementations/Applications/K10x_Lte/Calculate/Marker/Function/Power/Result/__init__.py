from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	@property
	def current(self):
		"""current commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_current'):
			from .Current import Current
			self._current = Current(self._core, self._cmd_group)
		return self._current

	@property
	def phz(self):
		"""phz commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phz'):
			from .Phz import Phz
			self._phz = Phz(self._core, self._cmd_group)
		return self._phz

	@property
	def unit(self):
		"""unit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_unit'):
			from .Unit import Unit
			self._unit = Unit(self._core, self._cmd_group)
		return self._unit

	def clone(self) -> 'Result':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Result(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
