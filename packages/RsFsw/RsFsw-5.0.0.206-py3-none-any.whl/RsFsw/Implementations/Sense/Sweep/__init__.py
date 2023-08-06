from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sweep:
	"""Sweep commands group definition. 37 total commands, 14 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sweep", core, parent)

	@property
	def points(self):
		"""points commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_points'):
			from .Points import Points
			self._points = Points(self._core, self._cmd_group)
		return self._points

	@property
	def scapture(self):
		"""scapture commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_scapture'):
			from .Scapture import Scapture
			self._scapture = Scapture(self._core, self._cmd_group)
		return self._scapture

	@property
	def time(self):
		"""time commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_time'):
			from .Time import Time
			self._time = Time(self._core, self._cmd_group)
		return self._time

	@property
	def fftSubspan(self):
		"""fftSubspan commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fftSubspan'):
			from .FftSubspan import FftSubspan
			self._fftSubspan = FftSubspan(self._core, self._cmd_group)
		return self._fftSubspan

	@property
	def egate(self):
		"""egate commands group. 8 Sub-classes, 1 commands."""
		if not hasattr(self, '_egate'):
			from .Egate import Egate
			self._egate = Egate(self._core, self._cmd_group)
		return self._egate

	@property
	def duration(self):
		"""duration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_duration'):
			from .Duration import Duration
			self._duration = Duration(self._core, self._cmd_group)
		return self._duration

	@property
	def window(self):
		"""window commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_window'):
			from .Window import Window
			self._window = Window(self._core, self._cmd_group)
		return self._window

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def typePy(self):
		"""typePy commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePy
			self._typePy = TypePy(self._core, self._cmd_group)
		return self._typePy

	@property
	def fft(self):
		"""fft commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fft'):
			from .Fft import Fft
			self._fft = Fft(self._core, self._cmd_group)
		return self._fft

	@property
	def ocapture(self):
		"""ocapture commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ocapture'):
			from .Ocapture import Ocapture
			self._ocapture = Ocapture(self._core, self._cmd_group)
		return self._ocapture

	@property
	def optimize(self):
		"""optimize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_optimize'):
			from .Optimize import Optimize
			self._optimize = Optimize(self._core, self._cmd_group)
		return self._optimize

	@property
	def dtime(self):
		"""dtime commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_dtime'):
			from .Dtime import Dtime
			self._dtime = Dtime(self._core, self._cmd_group)
		return self._dtime

	@property
	def count(self):
		"""count commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Count import Count
			self._count = Count(self._core, self._cmd_group)
		return self._count

	def clone(self) -> 'Sweep':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sweep(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
