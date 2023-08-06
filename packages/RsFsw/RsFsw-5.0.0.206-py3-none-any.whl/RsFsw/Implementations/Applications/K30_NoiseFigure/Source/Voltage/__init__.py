from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Voltage:
	"""Voltage commands group definition. 18 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("voltage", core, parent)

	@property
	def sequence(self):
		"""sequence commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sequence'):
			from .Sequence import Sequence
			self._sequence = Sequence(self._core, self._cmd_group)
		return self._sequence

	@property
	def auxiliary(self):
		"""auxiliary commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_auxiliary'):
			from .Auxiliary import Auxiliary
			self._auxiliary = Auxiliary(self._core, self._cmd_group)
		return self._auxiliary

	@property
	def channel(self):
		"""channel commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_channel'):
			from .Channel import Channel
			self._channel = Channel(self._core, self._cmd_group)
		return self._channel

	@property
	def control(self):
		"""control commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_control'):
			from .Control import Control
			self._control = Control(self._core, self._cmd_group)
		return self._control

	@property
	def power(self):
		"""power commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def usePort(self):
		"""usePort commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_usePort'):
			from .UsePort import UsePort
			self._usePort = UsePort(self._core, self._cmd_group)
		return self._usePort

	def clone(self) -> 'Voltage':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Voltage(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
