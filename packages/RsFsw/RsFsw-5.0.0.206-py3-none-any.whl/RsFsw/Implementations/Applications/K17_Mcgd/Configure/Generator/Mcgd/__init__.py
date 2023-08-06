from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mcgd:
	"""Mcgd commands group definition. 20 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcgd", core, parent)

	@property
	def aftm(self):
		"""aftm commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_aftm'):
			from .Aftm import Aftm
			self._aftm = Aftm(self._core, self._cmd_group)
		return self._aftm

	@property
	def control(self):
		"""control commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_control'):
			from .Control import Control
			self._control = Control(self._core, self._cmd_group)
		return self._control

	@property
	def carrier(self):
		"""carrier commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrier'):
			from .Carrier import Carrier
			self._carrier = Carrier(self._core, self._cmd_group)
		return self._carrier

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def connection(self):
		"""connection commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_connection'):
			from .Connection import Connection
			self._connection = Connection(self._core, self._cmd_group)
		return self._connection

	@property
	def ostate(self):
		"""ostate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ostate'):
			from .Ostate import Ostate
			self._ostate = Ostate(self._core, self._cmd_group)
		return self._ostate

	@property
	def level(self):
		"""level commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_level'):
			from .Level import Level
			self._level = Level(self._core, self._cmd_group)
		return self._level

	@property
	def settings(self):
		"""settings commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_settings'):
			from .Settings import Settings
			self._settings = Settings(self._core, self._cmd_group)
		return self._settings

	def clone(self) -> 'Mcgd':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mcgd(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
