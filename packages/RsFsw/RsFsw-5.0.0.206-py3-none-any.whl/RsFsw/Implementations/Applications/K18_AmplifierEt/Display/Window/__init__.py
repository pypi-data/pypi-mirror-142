from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Window:
	"""Window commands group definition. 36 total commands, 11 Subgroups, 0 group commands
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
	def minfo(self):
		"""minfo commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_minfo'):
			from .Minfo import Minfo
			self._minfo = Minfo(self._core, self._cmd_group)
		return self._minfo

	@property
	def mtable(self):
		"""mtable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mtable'):
			from .Mtable import Mtable
			self._mtable = Mtable(self._core, self._cmd_group)
		return self._mtable

	@property
	def psweep(self):
		"""psweep commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_psweep'):
			from .Psweep import Psweep
			self._psweep = Psweep(self._core, self._cmd_group)
		return self._psweep

	@property
	def ptable(self):
		"""ptable commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ptable'):
			from .Ptable import Ptable
			self._ptable = Ptable(self._core, self._cmd_group)
		return self._ptable

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

	@property
	def table(self):
		"""table commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_table'):
			from .Table import Table
			self._table = Table(self._core, self._cmd_group)
		return self._table

	@property
	def stable(self):
		"""stable commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_stable'):
			from .Stable import Stable
			self._stable = Stable(self._core, self._cmd_group)
		return self._stable

	@property
	def tdomain(self):
		"""tdomain commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tdomain'):
			from .Tdomain import Tdomain
			self._tdomain = Tdomain(self._core, self._cmd_group)
		return self._tdomain

	@property
	def subwindow(self):
		"""subwindow commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_subwindow'):
			from .Subwindow import Subwindow
			self._subwindow = Subwindow(self._core, self._cmd_group)
		return self._subwindow

	@property
	def trace(self):
		"""trace commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import Trace
			self._trace = Trace(self._core, self._cmd_group)
		return self._trace

	def clone(self) -> 'Window':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Window(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
