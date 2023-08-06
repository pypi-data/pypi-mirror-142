from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sequence:
	"""Sequence commands group definition. 6 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sequence", core, parent)

	@property
	def source(self):
		"""source commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_source'):
			from .Source import Source
			self._source = Source(self._core, self._cmd_group)
		return self._source

	@property
	def level(self):
		"""level commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_level'):
			from .Level import Level
			self._level = Level(self._core, self._cmd_group)
		return self._level

	@property
	def holdoff(self):
		"""holdoff commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_holdoff'):
			from .Holdoff import Holdoff
			self._holdoff = Holdoff(self._core, self._cmd_group)
		return self._holdoff

	@property
	def dtime(self):
		"""dtime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dtime'):
			from .Dtime import Dtime
			self._dtime = Dtime(self._core, self._cmd_group)
		return self._dtime

	@property
	def ifPower(self):
		"""ifPower commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ifPower'):
			from .IfPower import IfPower
			self._ifPower = IfPower(self._core, self._cmd_group)
		return self._ifPower

	@property
	def slope(self):
		"""slope commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_slope'):
			from .Slope import Slope
			self._slope = Slope(self._core, self._cmd_group)
		return self._slope

	def clone(self) -> 'Sequence':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sequence(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
