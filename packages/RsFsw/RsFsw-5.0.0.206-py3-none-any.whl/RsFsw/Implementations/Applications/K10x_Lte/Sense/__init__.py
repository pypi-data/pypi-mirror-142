from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sense:
	"""Sense commands group definition. 212 total commands, 16 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sense", core, parent)

	@property
	def lte(self):
		"""lte commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_lte'):
			from .Lte import Lte
			self._lte = Lte(self._core, self._cmd_group)
		return self._lte

	@property
	def adjust(self):
		"""adjust commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_adjust'):
			from .Adjust import Adjust
			self._adjust = Adjust(self._core, self._cmd_group)
		return self._adjust

	@property
	def average(self):
		"""average commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_average'):
			from .Average import Average
			self._average = Average(self._core, self._cmd_group)
		return self._average

	@property
	def bandwidth(self):
		"""bandwidth commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import Bandwidth
			self._bandwidth = Bandwidth(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def demod(self):
		"""demod commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_demod'):
			from .Demod import Demod
			self._demod = Demod(self._core, self._cmd_group)
		return self._demod

	@property
	def detector(self):
		"""detector commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_detector'):
			from .Detector import Detector
			self._detector = Detector(self._core, self._cmd_group)
		return self._detector

	@property
	def espectrum(self):
		"""espectrum commands group. 12 Sub-classes, 0 commands."""
		if not hasattr(self, '_espectrum'):
			from .Espectrum import Espectrum
			self._espectrum = Espectrum(self._core, self._cmd_group)
		return self._espectrum

	@property
	def frequency(self):
		"""frequency commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def inputPy(self):
		"""inputPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_inputPy'):
			from .InputPy import InputPy
			self._inputPy = InputPy(self._core, self._cmd_group)
		return self._inputPy

	@property
	def msra(self):
		"""msra commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_msra'):
			from .Msra import Msra
			self._msra = Msra(self._core, self._cmd_group)
		return self._msra

	@property
	def pmeter(self):
		"""pmeter commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_pmeter'):
			from .Pmeter import Pmeter
			self._pmeter = Pmeter(self._core, self._cmd_group)
		return self._pmeter

	@property
	def power(self):
		"""power commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def probe(self):
		"""probe commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_probe'):
			from .Probe import Probe
			self._probe = Probe(self._core, self._cmd_group)
		return self._probe

	@property
	def swapIq(self):
		"""swapIq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_swapIq'):
			from .SwapIq import SwapIq
			self._swapIq = SwapIq(self._core, self._cmd_group)
		return self._swapIq

	@property
	def sweep(self):
		"""sweep commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_sweep'):
			from .Sweep import Sweep
			self._sweep = Sweep(self._core, self._cmd_group)
		return self._sweep

	@property
	def sync(self):
		"""sync commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sync'):
			from .Sync import Sync
			self._sync = Sync(self._core, self._cmd_group)
		return self._sync

	def clone(self) -> 'Sense':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sense(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
