from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sense:
	"""Sense commands group definition. 486 total commands, 28 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sense", core, parent)

	@property
	def adjust(self):
		"""adjust commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_adjust'):
			from .Adjust import Adjust
			self._adjust = Adjust(self._core, self._cmd_group)
		return self._adjust

	@property
	def power(self):
		"""power commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def sweep(self):
		"""sweep commands group. 14 Sub-classes, 0 commands."""
		if not hasattr(self, '_sweep'):
			from .Sweep import Sweep
			self._sweep = Sweep(self._core, self._cmd_group)
		return self._sweep

	@property
	def mixer(self):
		"""mixer commands group. 11 Sub-classes, 0 commands."""
		if not hasattr(self, '_mixer'):
			from .Mixer import Mixer
			self._mixer = Mixer(self._core, self._cmd_group)
		return self._mixer

	@property
	def correction(self):
		"""correction commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_correction'):
			from .Correction import Correction
			self._correction = Correction(self._core, self._cmd_group)
		return self._correction

	@property
	def rlength(self):
		"""rlength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rlength'):
			from .Rlength import Rlength
			self._rlength = Rlength(self._core, self._cmd_group)
		return self._rlength

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRate
			self._symbolRate = SymbolRate(self._core, self._cmd_group)
		return self._symbolRate

	@property
	def swapIq(self):
		"""swapIq commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_swapIq'):
			from .SwapIq import SwapIq
			self._swapIq = SwapIq(self._core, self._cmd_group)
		return self._swapIq

	@property
	def ademod(self):
		"""ademod commands group. 12 Sub-classes, 0 commands."""
		if not hasattr(self, '_ademod'):
			from .Ademod import Ademod
			self._ademod = Ademod(self._core, self._cmd_group)
		return self._ademod

	@property
	def bandwidth(self):
		"""bandwidth commands group. 3 Sub-classes, 0 commands."""
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
	def ddemod(self):
		"""ddemod commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ddemod'):
			from .Ddemod import Ddemod
			self._ddemod = Ddemod(self._core, self._cmd_group)
		return self._ddemod

	@property
	def filterPy(self):
		"""filterPy commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._cmd_group)
		return self._filterPy

	@property
	def frequency(self):
		"""frequency commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def iq(self):
		"""iq commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iq'):
			from .Iq import Iq
			self._iq = Iq(self._core, self._cmd_group)
		return self._iq

	@property
	def listPy(self):
		"""listPy commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPy
			self._listPy = ListPy(self._core, self._cmd_group)
		return self._listPy

	@property
	def espectrum(self):
		"""espectrum commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_espectrum'):
			from .Espectrum import Espectrum
			self._espectrum = Espectrum(self._core, self._cmd_group)
		return self._espectrum

	@property
	def mpower(self):
		"""mpower commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_mpower'):
			from .Mpower import Mpower
			self._mpower = Mpower(self._core, self._cmd_group)
		return self._mpower

	@property
	def pmeter(self):
		"""pmeter commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_pmeter'):
			from .Pmeter import Pmeter
			self._pmeter = Pmeter(self._core, self._cmd_group)
		return self._pmeter

	@property
	def probe(self):
		"""probe commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_probe'):
			from .Probe import Probe
			self._probe = Probe(self._core, self._cmd_group)
		return self._probe

	@property
	def npratio(self):
		"""npratio commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_npratio'):
			from .Npratio import Npratio
			self._npratio = Npratio(self._core, self._cmd_group)
		return self._npratio

	@property
	def roscillator(self):
		"""roscillator commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_roscillator'):
			from .Roscillator import Roscillator
			self._roscillator = Roscillator(self._core, self._cmd_group)
		return self._roscillator

	@property
	def sampling(self):
		"""sampling commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sampling'):
			from .Sampling import Sampling
			self._sampling = Sampling(self._core, self._cmd_group)
		return self._sampling

	@property
	def trace(self):
		"""trace commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import Trace
			self._trace = Trace(self._core, self._cmd_group)
		return self._trace

	@property
	def average(self):
		"""average commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_average'):
			from .Average import Average
			self._average = Average(self._core, self._cmd_group)
		return self._average

	@property
	def msra(self):
		"""msra commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_msra'):
			from .Msra import Msra
			self._msra = Msra(self._core, self._cmd_group)
		return self._msra

	@property
	def rtms(self):
		"""rtms commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rtms'):
			from .Rtms import Rtms
			self._rtms = Rtms(self._core, self._cmd_group)
		return self._rtms

	@property
	def window(self):
		"""window commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_window'):
			from .Window import Window
			self._window = Window(self._core, self._cmd_group)
		return self._window

	def clone(self) -> 'Sense':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sense(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
