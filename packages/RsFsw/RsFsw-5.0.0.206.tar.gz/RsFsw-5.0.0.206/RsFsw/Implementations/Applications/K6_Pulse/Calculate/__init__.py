from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Calculate:
	"""Calculate commands group definition. 285 total commands, 12 Subgroups, 0 group commands
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
	def unit(self):
		"""unit commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_unit'):
			from .Unit import Unit
			self._unit = Unit(self._core, self._cmd_group)
		return self._unit

	@property
	def deltaMarker(self):
		"""deltaMarker commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_deltaMarker'):
			from .DeltaMarker import DeltaMarker
			self._deltaMarker = DeltaMarker(self._core, self._cmd_group)
		return self._deltaMarker

	@property
	def distribution(self):
		"""distribution commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_distribution'):
			from .Distribution import Distribution
			self._distribution = Distribution(self._core, self._cmd_group)
		return self._distribution

	@property
	def marker(self):
		"""marker commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_marker'):
			from .Marker import Marker
			self._marker = Marker(self._core, self._cmd_group)
		return self._marker

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
	def trace(self):
		"""trace commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import Trace
			self._trace = Trace(self._core, self._cmd_group)
		return self._trace

	@property
	def table(self):
		"""table commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_table'):
			from .Table import Table
			self._table = Table(self._core, self._cmd_group)
		return self._table

	@property
	def pspectrum(self):
		"""pspectrum commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_pspectrum'):
			from .Pspectrum import Pspectrum
			self._pspectrum = Pspectrum(self._core, self._cmd_group)
		return self._pspectrum

	@property
	def ppSpectrum(self):
		"""ppSpectrum commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_ppSpectrum'):
			from .PpSpectrum import PpSpectrum
			self._ppSpectrum = PpSpectrum(self._core, self._cmd_group)
		return self._ppSpectrum

	@property
	def rrSpectrum(self):
		"""rrSpectrum commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_rrSpectrum'):
			from .RrSpectrum import RrSpectrum
			self._rrSpectrum = RrSpectrum(self._core, self._cmd_group)
		return self._rrSpectrum

	@property
	def trend(self):
		"""trend commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_trend'):
			from .Trend import Trend
			self._trend = Trend(self._core, self._cmd_group)
		return self._trend

	def clone(self) -> 'Calculate':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Calculate(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
