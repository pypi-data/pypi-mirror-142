from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal.RepeatedCapability import RepeatedCapability
from ... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Calculate:
	"""Calculate commands group definition. 359 total commands, 22 Subgroups, 0 group commands
	Repeated Capability: Window, default value after init: Window.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("calculate", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_window_get', 'repcap_window_set', repcap.Window.Nr1)

	def repcap_window_set(self, window: repcap.Window) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Window.Default
		Default value after init: Window.Nr1"""
		self._cmd_group.set_repcap_enum_value(window)

	def repcap_window_get(self) -> repcap.Window:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def deltaMarker(self):
		"""deltaMarker commands group. 14 Sub-classes, 0 commands."""
		if not hasattr(self, '_deltaMarker'):
			from .DeltaMarker import DeltaMarker
			self._deltaMarker = DeltaMarker(self._core, self._cmd_group)
		return self._deltaMarker

	@property
	def marker(self):
		"""marker commands group. 16 Sub-classes, 0 commands."""
		if not hasattr(self, '_marker'):
			from .Marker import Marker
			self._marker = Marker(self._core, self._cmd_group)
		return self._marker

	@property
	def limit(self):
		"""limit commands group. 14 Sub-classes, 1 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import Limit
			self._limit = Limit(self._core, self._cmd_group)
		return self._limit

	@property
	def msra(self):
		"""msra commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_msra'):
			from .Msra import Msra
			self._msra = Msra(self._core, self._cmd_group)
		return self._msra

	@property
	def rtms(self):
		"""rtms commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rtms'):
			from .Rtms import Rtms
			self._rtms = Rtms(self._core, self._cmd_group)
		return self._rtms

	@property
	def unit(self):
		"""unit commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_unit'):
			from .Unit import Unit
			self._unit = Unit(self._core, self._cmd_group)
		return self._unit

	@property
	def espectrum(self):
		"""espectrum commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_espectrum'):
			from .Espectrum import Espectrum
			self._espectrum = Espectrum(self._core, self._cmd_group)
		return self._espectrum

	@property
	def feed(self):
		"""feed commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_feed'):
			from .Feed import Feed
			self._feed = Feed(self._core, self._cmd_group)
		return self._feed

	@property
	def formatPy(self):
		"""formatPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPy
			self._formatPy = FormatPy(self._core, self._cmd_group)
		return self._formatPy

	@property
	def iq(self):
		"""iq commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iq'):
			from .Iq import Iq
			self._iq = Iq(self._core, self._cmd_group)
		return self._iq

	@property
	def mask(self):
		"""mask commands group. 7 Sub-classes, 1 commands."""
		if not hasattr(self, '_mask'):
			from .Mask import Mask
			self._mask = Mask(self._core, self._cmd_group)
		return self._mask

	@property
	def math(self):
		"""math commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_math'):
			from .Math import Math
			self._math = Math(self._core, self._cmd_group)
		return self._math

	@property
	def npratio(self):
		"""npratio commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_npratio'):
			from .Npratio import Npratio
			self._npratio = Npratio(self._core, self._cmd_group)
		return self._npratio

	@property
	def peakSearch(self):
		"""peakSearch commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_peakSearch'):
			from .PeakSearch import PeakSearch
			self._peakSearch = PeakSearch(self._core, self._cmd_group)
		return self._peakSearch

	@property
	def pmeter(self):
		"""pmeter commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pmeter'):
			from .Pmeter import Pmeter
			self._pmeter = Pmeter(self._core, self._cmd_group)
		return self._pmeter

	@property
	def spectrogram(self):
		"""spectrogram commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_spectrogram'):
			from .Spectrogram import Spectrogram
			self._spectrogram = Spectrogram(self._core, self._cmd_group)
		return self._spectrogram

	@property
	def statistics(self):
		"""statistics commands group. 5 Sub-classes, 1 commands."""
		if not hasattr(self, '_statistics'):
			from .Statistics import Statistics
			self._statistics = Statistics(self._core, self._cmd_group)
		return self._statistics

	@property
	def dline(self):
		"""dline commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_dline'):
			from .Dline import Dline
			self._dline = Dline(self._core, self._cmd_group)
		return self._dline

	@property
	def threshold(self):
		"""threshold commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_threshold'):
			from .Threshold import Threshold
			self._threshold = Threshold(self._core, self._cmd_group)
		return self._threshold

	@property
	def fline(self):
		"""fline commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_fline'):
			from .Fline import Fline
			self._fline = Fline(self._core, self._cmd_group)
		return self._fline

	@property
	def pline(self):
		"""pline commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_pline'):
			from .Pline import Pline
			self._pline = Pline(self._core, self._cmd_group)
		return self._pline

	@property
	def tline(self):
		"""tline commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_tline'):
			from .Tline import Tline
			self._tline = Tline(self._core, self._cmd_group)
		return self._tline

	def clone(self) -> 'Calculate':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Calculate(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
