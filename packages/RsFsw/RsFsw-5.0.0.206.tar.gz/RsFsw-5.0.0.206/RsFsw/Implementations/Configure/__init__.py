from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Configure:
	"""Configure commands group definition. 63 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("configure", core, parent)

	@property
	def ademod(self):
		"""ademod commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ademod'):
			from .Ademod import Ademod
			self._ademod = Ademod(self._core, self._cmd_group)
		return self._ademod

	@property
	def generator(self):
		"""generator commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_generator'):
			from .Generator import Generator
			self._generator = Generator(self._core, self._cmd_group)
		return self._generator

	@property
	def settings(self):
		"""settings commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_settings'):
			from .Settings import Settings
			self._settings = Settings(self._core, self._cmd_group)
		return self._settings

	@property
	def cmeasurement(self):
		"""cmeasurement commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cmeasurement'):
			from .Cmeasurement import Cmeasurement
			self._cmeasurement = Cmeasurement(self._core, self._cmd_group)
		return self._cmeasurement

	@property
	def realtime(self):
		"""realtime commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_realtime'):
			from .Realtime import Realtime
			self._realtime = Realtime(self._core, self._cmd_group)
		return self._realtime

	def clone(self) -> 'Configure':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Configure(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
