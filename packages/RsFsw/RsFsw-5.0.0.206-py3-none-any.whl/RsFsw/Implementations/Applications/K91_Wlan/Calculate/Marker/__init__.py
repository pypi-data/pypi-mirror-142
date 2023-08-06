from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Marker:
	"""Marker commands group definition. 21 total commands, 11 Subgroups, 0 group commands
	Repeated Capability: Marker, default value after init: Marker.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("marker", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_marker_get', 'repcap_marker_set', repcap.Marker.Nr1)

	def repcap_marker_set(self, marker: repcap.Marker) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Marker.Default
		Default value after init: Marker.Nr1"""
		self._cmd_group.set_repcap_enum_value(marker)

	def repcap_marker_get(self) -> repcap.Marker:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def y(self):
		"""y commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_y'):
			from .Y import Y
			self._y = Y(self._core, self._cmd_group)
		return self._y

	@property
	def function(self):
		"""function commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_function'):
			from .Function import Function
			self._function = Function(self._core, self._cmd_group)
		return self._function

	@property
	def aoff(self):
		"""aoff commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aoff'):
			from .Aoff import Aoff
			self._aoff = Aoff(self._core, self._cmd_group)
		return self._aoff

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def trace(self):
		"""trace commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import Trace
			self._trace = Trace(self._core, self._cmd_group)
		return self._trace

	@property
	def x(self):
		"""x commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_x'):
			from .X import X
			self._x = X(self._core, self._cmd_group)
		return self._x

	@property
	def loExclude(self):
		"""loExclude commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_loExclude'):
			from .LoExclude import LoExclude
			self._loExclude = LoExclude(self._core, self._cmd_group)
		return self._loExclude

	@property
	def pexcursion(self):
		"""pexcursion commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pexcursion'):
			from .Pexcursion import Pexcursion
			self._pexcursion = Pexcursion(self._core, self._cmd_group)
		return self._pexcursion

	@property
	def symbol(self):
		"""symbol commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbol'):
			from .Symbol import Symbol
			self._symbol = Symbol(self._core, self._cmd_group)
		return self._symbol

	@property
	def carrier(self):
		"""carrier commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_carrier'):
			from .Carrier import Carrier
			self._carrier = Carrier(self._core, self._cmd_group)
		return self._carrier

	@property
	def bsymbol(self):
		"""bsymbol commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bsymbol'):
			from .Bsymbol import Bsymbol
			self._bsymbol = Bsymbol(self._core, self._cmd_group)
		return self._bsymbol

	def clone(self) -> 'Marker':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Marker(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
