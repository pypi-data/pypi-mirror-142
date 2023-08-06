from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Couple:
	"""Couple commands group definition. 21 total commands, 17 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("couple", core, parent)

	@property
	def center(self):
		"""center commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_center'):
			from .Center import Center
			self._center = Center(self._core, self._cmd_group)
		return self._center

	@property
	def span(self):
		"""span commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_span'):
			from .Span import Span
			self._span = Span(self._core, self._cmd_group)
		return self._span

	@property
	def refLevel(self):
		"""refLevel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_refLevel'):
			from .RefLevel import RefLevel
			self._refLevel = RefLevel(self._core, self._cmd_group)
		return self._refLevel

	@property
	def atten(self):
		"""atten commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_atten'):
			from .Atten import Atten
			self._atten = Atten(self._core, self._cmd_group)
		return self._atten

	@property
	def gain(self):
		"""gain commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gain'):
			from .Gain import Gain
			self._gain = Gain(self._core, self._cmd_group)
		return self._gain

	@property
	def presel(self):
		"""presel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_presel'):
			from .Presel import Presel
			self._presel = Presel(self._core, self._cmd_group)
		return self._presel

	@property
	def demod(self):
		"""demod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_demod'):
			from .Demod import Demod
			self._demod = Demod(self._core, self._cmd_group)
		return self._demod

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import Bandwidth
			self._bandwidth = Bandwidth(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def vbw(self):
		"""vbw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vbw'):
			from .Vbw import Vbw
			self._vbw = Vbw(self._core, self._cmd_group)
		return self._vbw

	@property
	def llines(self):
		"""llines commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_llines'):
			from .Llines import Llines
			self._llines = Llines(self._core, self._cmd_group)
		return self._llines

	@property
	def limit(self):
		"""limit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import Limit
			self._limit = Limit(self._core, self._cmd_group)
		return self._limit

	@property
	def acDc(self):
		"""acDc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_acDc'):
			from .AcDc import AcDc
			self._acDc = AcDc(self._core, self._cmd_group)
		return self._acDc

	@property
	def aunit(self):
		"""aunit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aunit'):
			from .Aunit import Aunit
			self._aunit = Aunit(self._core, self._cmd_group)
		return self._aunit

	@property
	def impedance(self):
		"""impedance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_impedance'):
			from .Impedance import Impedance
			self._impedance = Impedance(self._core, self._cmd_group)
		return self._impedance

	@property
	def abImpedance(self):
		"""abImpedance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_abImpedance'):
			from .AbImpedance import AbImpedance
			self._abImpedance = AbImpedance(self._core, self._cmd_group)
		return self._abImpedance

	@property
	def marker(self):
		"""marker commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_marker'):
			from .Marker import Marker
			self._marker = Marker(self._core, self._cmd_group)
		return self._marker

	@property
	def generator(self):
		"""generator commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_generator'):
			from .Generator import Generator
			self._generator = Generator(self._core, self._cmd_group)
		return self._generator

	def clone(self) -> 'Couple':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Couple(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
