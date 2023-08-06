from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sense:
	"""Sense commands group definition. 68 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sense", core, parent)

	@property
	def adjust(self):
		"""adjust commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_adjust'):
			from .Adjust import Adjust
			self._adjust = Adjust(self._core, self._cmd_group)
		return self._adjust

	@property
	def correction(self):
		"""correction commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_correction'):
			from .Correction import Correction
			self._correction = Correction(self._core, self._cmd_group)
		return self._correction

	@property
	def frequency(self):
		"""frequency commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def swapIq(self):
		"""swapIq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_swapIq'):
			from .SwapIq import SwapIq
			self._swapIq = SwapIq(self._core, self._cmd_group)
		return self._swapIq

	@property
	def sweep(self):
		"""sweep commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_sweep'):
			from .Sweep import Sweep
			self._sweep = Sweep(self._core, self._cmd_group)
		return self._sweep

	@property
	def tracking(self):
		"""tracking commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_tracking'):
			from .Tracking import Tracking
			self._tracking = Tracking(self._core, self._cmd_group)
		return self._tracking

	@property
	def pmeter(self):
		"""pmeter commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_pmeter'):
			from .Pmeter import Pmeter
			self._pmeter = Pmeter(self._core, self._cmd_group)
		return self._pmeter

	@property
	def burst(self):
		"""burst commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_burst'):
			from .Burst import Burst
			self._burst = Burst(self._core, self._cmd_group)
		return self._burst

	@property
	def demod(self):
		"""demod commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_demod'):
			from .Demod import Demod
			self._demod = Demod(self._core, self._cmd_group)
		return self._demod

	@property
	def mixer(self):
		"""mixer commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_mixer'):
			from .Mixer import Mixer
			self._mixer = Mixer(self._core, self._cmd_group)
		return self._mixer

	def clone(self) -> 'Sense':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sense(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
