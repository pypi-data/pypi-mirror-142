from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Generator:
	"""Generator commands group definition. 11 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("generator", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def power(self):
		"""power commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def level(self):
		"""level commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_level'):
			from .Level import Level
			self._level = Level(self._core, self._cmd_group)
		return self._level

	@property
	def qerror(self):
		"""qerror commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_qerror'):
			from .Qerror import Qerror
			self._qerror = Qerror(self._core, self._cmd_group)
		return self._qerror

	@property
	def rfOutput(self):
		"""rfOutput commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfOutput'):
			from .RfOutput import RfOutput
			self._rfOutput = RfOutput(self._core, self._cmd_group)
		return self._rfOutput

	@property
	def control(self):
		"""control commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_control'):
			from .Control import Control
			self._control = Control(self._core, self._cmd_group)
		return self._control

	@property
	def settings(self):
		"""settings commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_settings'):
			from .Settings import Settings
			self._settings = Settings(self._core, self._cmd_group)
		return self._settings

	def clone(self) -> 'Generator':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Generator(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
