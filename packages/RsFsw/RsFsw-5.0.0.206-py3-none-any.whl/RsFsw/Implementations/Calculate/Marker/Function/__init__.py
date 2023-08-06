from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Function:
	"""Function commands group definition. 108 total commands, 19 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("function", core, parent)

	@property
	def afPhase(self):
		"""afPhase commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_afPhase'):
			from .AfPhase import AfPhase
			self._afPhase = AfPhase(self._core, self._cmd_group)
		return self._afPhase

	@property
	def demodulation(self):
		"""demodulation commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_demodulation'):
			from .Demodulation import Demodulation
			self._demodulation = Demodulation(self._core, self._cmd_group)
		return self._demodulation

	@property
	def fpeaks(self):
		"""fpeaks commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_fpeaks'):
			from .Fpeaks import Fpeaks
			self._fpeaks = Fpeaks(self._core, self._cmd_group)
		return self._fpeaks

	@property
	def ndbDown(self):
		"""ndbDown commands group. 5 Sub-classes, 1 commands."""
		if not hasattr(self, '_ndbDown'):
			from .NdbDown import NdbDown
			self._ndbDown = NdbDown(self._core, self._cmd_group)
		return self._ndbDown

	@property
	def noise(self):
		"""noise commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_noise'):
			from .Noise import Noise
			self._noise = Noise(self._core, self._cmd_group)
		return self._noise

	@property
	def pnoise(self):
		"""pnoise commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pnoise'):
			from .Pnoise import Pnoise
			self._pnoise = Pnoise(self._core, self._cmd_group)
		return self._pnoise

	@property
	def mdepth(self):
		"""mdepth commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_mdepth'):
			from .Mdepth import Mdepth
			self._mdepth = Mdepth(self._core, self._cmd_group)
		return self._mdepth

	@property
	def toi(self):
		"""toi commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_toi'):
			from .Toi import Toi
			self._toi = Toi(self._core, self._cmd_group)
		return self._toi

	@property
	def bpower(self):
		"""bpower commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_bpower'):
			from .Bpower import Bpower
			self._bpower = Bpower(self._core, self._cmd_group)
		return self._bpower

	@property
	def center(self):
		"""center commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_center'):
			from .Center import Center
			self._center = Center(self._core, self._cmd_group)
		return self._center

	@property
	def cstep(self):
		"""cstep commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cstep'):
			from .Cstep import Cstep
			self._cstep = Cstep(self._core, self._cmd_group)
		return self._cstep

	@property
	def reference(self):
		"""reference commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_reference'):
			from .Reference import Reference
			self._reference = Reference(self._core, self._cmd_group)
		return self._reference

	@property
	def fmeasurement(self):
		"""fmeasurement commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_fmeasurement'):
			from .Fmeasurement import Fmeasurement
			self._fmeasurement = Fmeasurement(self._core, self._cmd_group)
		return self._fmeasurement

	@property
	def ademod(self):
		"""ademod commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_ademod'):
			from .Ademod import Ademod
			self._ademod = Ademod(self._core, self._cmd_group)
		return self._ademod

	@property
	def power(self):
		"""power commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def strack(self):
		"""strack commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_strack'):
			from .Strack import Strack
			self._strack = Strack(self._core, self._cmd_group)
		return self._strack

	@property
	def summary(self):
		"""summary commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_summary'):
			from .Summary import Summary
			self._summary = Summary(self._core, self._cmd_group)
		return self._summary

	@property
	def msummary(self):
		"""msummary commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_msummary'):
			from .Msummary import Msummary
			self._msummary = Msummary(self._core, self._cmd_group)
		return self._msummary

	@property
	def harmonics(self):
		"""harmonics commands group. 5 Sub-classes, 1 commands."""
		if not hasattr(self, '_harmonics'):
			from .Harmonics import Harmonics
			self._harmonics = Harmonics(self._core, self._cmd_group)
		return self._harmonics

	def clone(self) -> 'Function':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Function(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
