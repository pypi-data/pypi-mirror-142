from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Generator:
	"""Generator commands group definition. 25 total commands, 11 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("generator", core, parent)

	@property
	def control(self):
		"""control commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_control'):
			from .Control import Control
			self._control = Control(self._core, self._cmd_group)
		return self._control

	@property
	def external(self):
		"""external commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_external'):
			from .External import External
			self._external = External(self._core, self._cmd_group)
		return self._external

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def ipConnection(self):
		"""ipConnection commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipConnection'):
			from .IpConnection import IpConnection
			self._ipConnection = IpConnection(self._core, self._cmd_group)
		return self._ipConnection

	@property
	def power(self):
		"""power commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def level(self):
		"""level commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_level'):
			from .Level import Level
			self._level = Level(self._core, self._cmd_group)
		return self._level

	@property
	def dut(self):
		"""dut commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dut'):
			from .Dut import Dut
			self._dut = Dut(self._core, self._cmd_group)
		return self._dut

	@property
	def rfOutput(self):
		"""rfOutput commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfOutput'):
			from .RfOutput import RfOutput
			self._rfOutput = RfOutput(self._core, self._cmd_group)
		return self._rfOutput

	@property
	def segment(self):
		"""segment commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_segment'):
			from .Segment import Segment
			self._segment = Segment(self._core, self._cmd_group)
		return self._segment

	@property
	def settings(self):
		"""settings commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_settings'):
			from .Settings import Settings
			self._settings = Settings(self._core, self._cmd_group)
		return self._settings

	@property
	def target(self):
		"""target commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_target'):
			from .Target import Target
			self._target = Target(self._core, self._cmd_group)
		return self._target

	def clone(self) -> 'Generator':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Generator(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
