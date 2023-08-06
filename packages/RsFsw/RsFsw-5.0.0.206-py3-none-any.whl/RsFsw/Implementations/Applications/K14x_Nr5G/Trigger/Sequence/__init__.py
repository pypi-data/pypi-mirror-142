from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sequence:
	"""Sequence commands group definition. 15 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sequence", core, parent)

	@property
	def bbPower(self):
		"""bbPower commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bbPower'):
			from .BbPower import BbPower
			self._bbPower = BbPower(self._core, self._cmd_group)
		return self._bbPower

	@property
	def dtime(self):
		"""dtime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dtime'):
			from .Dtime import Dtime
			self._dtime = Dtime(self._core, self._cmd_group)
		return self._dtime

	@property
	def holdoff(self):
		"""holdoff commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_holdoff'):
			from .Holdoff import Holdoff
			self._holdoff = Holdoff(self._core, self._cmd_group)
		return self._holdoff

	@property
	def ifPower(self):
		"""ifPower commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ifPower'):
			from .IfPower import IfPower
			self._ifPower = IfPower(self._core, self._cmd_group)
		return self._ifPower

	@property
	def level(self):
		"""level commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_level'):
			from .Level import Level
			self._level = Level(self._core, self._cmd_group)
		return self._level

	@property
	def port(self):
		"""port commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_port'):
			from .Port import Port
			self._port = Port(self._core, self._cmd_group)
		return self._port

	@property
	def rfPower(self):
		"""rfPower commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfPower'):
			from .RfPower import RfPower
			self._rfPower = RfPower(self._core, self._cmd_group)
		return self._rfPower

	@property
	def slope(self):
		"""slope commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_slope'):
			from .Slope import Slope
			self._slope = Slope(self._core, self._cmd_group)
		return self._slope

	@property
	def source(self):
		"""source commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_source'):
			from .Source import Source
			self._source = Source(self._core, self._cmd_group)
		return self._source

	@property
	def time(self):
		"""time commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_time'):
			from .Time import Time
			self._time = Time(self._core, self._cmd_group)
		return self._time

	def clone(self) -> 'Sequence':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sequence(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
