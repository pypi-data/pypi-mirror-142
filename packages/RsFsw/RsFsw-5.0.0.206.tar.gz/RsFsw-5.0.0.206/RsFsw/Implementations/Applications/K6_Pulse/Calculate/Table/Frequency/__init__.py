from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 20 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	@property
	def all(self):
		"""all commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	@property
	def crate(self):
		"""crate commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_crate'):
			from .Crate import Crate
			self._crate = Crate(self._core, self._cmd_group)
		return self._crate

	@property
	def deviation(self):
		"""deviation commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_deviation'):
			from .Deviation import Deviation
			self._deviation = Deviation(self._core, self._cmd_group)
		return self._deviation

	@property
	def perror(self):
		"""perror commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_perror'):
			from .Perror import Perror
			self._perror = Perror(self._core, self._cmd_group)
		return self._perror

	@property
	def point(self):
		"""point commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_point'):
			from .Point import Point
			self._point = Point(self._core, self._cmd_group)
		return self._point

	@property
	def ppFrequency(self):
		"""ppFrequency commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ppFrequency'):
			from .PpFrequency import PpFrequency
			self._ppFrequency = PpFrequency(self._core, self._cmd_group)
		return self._ppFrequency

	@property
	def rerror(self):
		"""rerror commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_rerror'):
			from .Rerror import Rerror
			self._rerror = Rerror(self._core, self._cmd_group)
		return self._rerror

	def clone(self) -> 'Frequency':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Frequency(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
