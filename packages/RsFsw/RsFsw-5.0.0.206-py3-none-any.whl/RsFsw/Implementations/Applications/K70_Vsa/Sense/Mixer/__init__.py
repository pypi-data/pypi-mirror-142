from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mixer:
	"""Mixer commands group definition. 18 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mixer", core, parent)

	@property
	def loPower(self):
		"""loPower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_loPower'):
			from .LoPower import LoPower
			self._loPower = LoPower(self._core, self._cmd_group)
		return self._loPower

	@property
	def ports(self):
		"""ports commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ports'):
			from .Ports import Ports
			self._ports = Ports(self._core, self._cmd_group)
		return self._ports

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def bias(self):
		"""bias commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_bias'):
			from .Bias import Bias
			self._bias = Bias(self._core, self._cmd_group)
		return self._bias

	@property
	def frequency(self):
		"""frequency commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def harmonic(self):
		"""harmonic commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_harmonic'):
			from .Harmonic import Harmonic
			self._harmonic = Harmonic(self._core, self._cmd_group)
		return self._harmonic

	@property
	def loss(self):
		"""loss commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_loss'):
			from .Loss import Loss
			self._loss = Loss(self._core, self._cmd_group)
		return self._loss

	@property
	def rfOverrange(self):
		"""rfOverrange commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfOverrange'):
			from .RfOverrange import RfOverrange
			self._rfOverrange = RfOverrange(self._core, self._cmd_group)
		return self._rfOverrange

	def clone(self) -> 'Mixer':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mixer(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
