from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.RepeatedCapability import RepeatedCapability
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Calculate:
	"""Calculate commands group definition. 213 total commands, 22 Subgroups, 0 group commands
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
	def bitErrorRate(self):
		"""bitErrorRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bitErrorRate'):
			from .BitErrorRate import BitErrorRate
			self._bitErrorRate = BitErrorRate(self._core, self._cmd_group)
		return self._bitErrorRate

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
	def ddem(self):
		"""ddem commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ddem'):
			from .Ddem import Ddem
			self._ddem = Ddem(self._core, self._cmd_group)
		return self._ddem

	@property
	def dlabs(self):
		"""dlabs commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dlabs'):
			from .Dlabs import Dlabs
			self._dlabs = Dlabs(self._core, self._cmd_group)
		return self._dlabs

	@property
	def dlRel(self):
		"""dlRel commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dlRel'):
			from .DlRel import DlRel
			self._dlRel = DlRel(self._core, self._cmd_group)
		return self._dlRel

	@property
	def dsp(self):
		"""dsp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dsp'):
			from .Dsp import Dsp
			self._dsp = Dsp(self._core, self._cmd_group)
		return self._dsp

	@property
	def meas(self):
		"""meas commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_meas'):
			from .Meas import Meas
			self._meas = Meas(self._core, self._cmd_group)
		return self._meas

	@property
	def elin(self):
		"""elin commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_elin'):
			from .Elin import Elin
			self._elin = Elin(self._core, self._cmd_group)
		return self._elin

	@property
	def fsk(self):
		"""fsk commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fsk'):
			from .Fsk import Fsk
			self._fsk = Fsk(self._core, self._cmd_group)
		return self._fsk

	@property
	def limit(self):
		"""limit commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import Limit
			self._limit = Limit(self._core, self._cmd_group)
		return self._limit

	@property
	def marker(self):
		"""marker commands group. 11 Sub-classes, 0 commands."""
		if not hasattr(self, '_marker'):
			from .Marker import Marker
			self._marker = Marker(self._core, self._cmd_group)
		return self._marker

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
	def deltaMarker(self):
		"""deltaMarker commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_deltaMarker'):
			from .DeltaMarker import DeltaMarker
			self._deltaMarker = DeltaMarker(self._core, self._cmd_group)
		return self._deltaMarker

	@property
	def statistics(self):
		"""statistics commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_statistics'):
			from .Statistics import Statistics
			self._statistics = Statistics(self._core, self._cmd_group)
		return self._statistics

	@property
	def tlRel(self):
		"""tlRel commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tlRel'):
			from .TlRel import TlRel
			self._tlRel = TlRel(self._core, self._cmd_group)
		return self._tlRel

	@property
	def tlAbs(self):
		"""tlAbs commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tlAbs'):
			from .TlAbs import TlAbs
			self._tlAbs = TlAbs(self._core, self._cmd_group)
		return self._tlAbs

	@property
	def trace(self):
		"""trace commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import Trace
			self._trace = Trace(self._core, self._cmd_group)
		return self._trace

	@property
	def unit(self):
		"""unit commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_unit'):
			from .Unit import Unit
			self._unit = Unit(self._core, self._cmd_group)
		return self._unit

	@property
	def x(self):
		"""x commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_x'):
			from .X import X
			self._x = X(self._core, self._cmd_group)
		return self._x

	@property
	def y(self):
		"""y commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_y'):
			from .Y import Y
			self._y = Y(self._core, self._cmd_group)
		return self._y

	def clone(self) -> 'Calculate':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Calculate(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
