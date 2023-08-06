from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Results:
	"""Results commands group definition. 17 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("results", core, parent)

	@property
	def am(self):
		"""am commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_am'):
			from .Am import Am
			self._am = Am(self._core, self._cmd_group)
		return self._am

	@property
	def acv(self):
		"""acv commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_acv'):
			from .Acv import Acv
			self._acv = Acv(self._core, self._cmd_group)
		return self._acv

	@property
	def fm(self):
		"""fm commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fm'):
			from .Fm import Fm
			self._fm = Fm(self._core, self._cmd_group)
		return self._fm

	@property
	def pm(self):
		"""pm commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pm'):
			from .Pm import Pm
			self._pm = Pm(self._core, self._cmd_group)
		return self._pm

	@property
	def unit(self):
		"""unit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_unit'):
			from .Unit import Unit
			self._unit = Unit(self._core, self._cmd_group)
		return self._unit

	def clone(self) -> 'Results':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Results(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
