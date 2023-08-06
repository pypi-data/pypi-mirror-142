from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Window:
	"""Window commands group definition. 66 total commands, 9 Subgroups, 0 group commands
	Repeated Capability: Window, default value after init: Window.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("window", core, parent)
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
	def trace(self):
		"""trace commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import Trace
			self._trace = Trace(self._core, self._cmd_group)
		return self._trace

	@property
	def minfo(self):
		"""minfo commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_minfo'):
			from .Minfo import Minfo
			self._minfo = Minfo(self._core, self._cmd_group)
		return self._minfo

	@property
	def subwindow(self):
		"""subwindow commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_subwindow'):
			from .Subwindow import Subwindow
			self._subwindow = Subwindow(self._core, self._cmd_group)
		return self._subwindow

	@property
	def pspectrum(self):
		"""pspectrum commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pspectrum'):
			from .Pspectrum import Pspectrum
			self._pspectrum = Pspectrum(self._core, self._cmd_group)
		return self._pspectrum

	@property
	def spectrogram(self):
		"""spectrogram commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_spectrogram'):
			from .Spectrogram import Spectrogram
			self._spectrogram = Spectrogram(self._core, self._cmd_group)
		return self._spectrogram

	@property
	def time(self):
		"""time commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_time'):
			from .Time import Time
			self._time = Time(self._core, self._cmd_group)
		return self._time

	@property
	def mtable(self):
		"""mtable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mtable'):
			from .Mtable import Mtable
			self._mtable = Mtable(self._core, self._cmd_group)
		return self._mtable

	@property
	def size(self):
		"""size commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_size'):
			from .Size import Size
			self._size = Size(self._core, self._cmd_group)
		return self._size

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'Window':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Window(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
