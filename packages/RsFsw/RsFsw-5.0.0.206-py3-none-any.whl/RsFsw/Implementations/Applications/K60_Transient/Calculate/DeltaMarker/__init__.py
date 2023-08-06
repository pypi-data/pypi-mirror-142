from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DeltaMarker:
	"""DeltaMarker commands group definition. 28 total commands, 10 Subgroups, 0 group commands
	Repeated Capability: DeltaMarker, default value after init: DeltaMarker.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("deltaMarker", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_deltaMarker_get', 'repcap_deltaMarker_set', repcap.DeltaMarker.Nr1)

	def repcap_deltaMarker_set(self, deltaMarker: repcap.DeltaMarker) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to DeltaMarker.Default
		Default value after init: DeltaMarker.Nr1"""
		self._cmd_group.set_repcap_enum_value(deltaMarker)

	def repcap_deltaMarker_get(self) -> repcap.DeltaMarker:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def aoff(self):
		"""aoff commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aoff'):
			from .Aoff import Aoff
			self._aoff = Aoff(self._core, self._cmd_group)
		return self._aoff

	@property
	def linkTo(self):
		"""linkTo commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_linkTo'):
			from .LinkTo import LinkTo
			self._linkTo = LinkTo(self._core, self._cmd_group)
		return self._linkTo

	@property
	def maximum(self):
		"""maximum commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_maximum'):
			from .Maximum import Maximum
			self._maximum = Maximum(self._core, self._cmd_group)
		return self._maximum

	@property
	def minimum(self):
		"""minimum commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_minimum'):
			from .Minimum import Minimum
			self._minimum = Minimum(self._core, self._cmd_group)
		return self._minimum

	@property
	def mreference(self):
		"""mreference commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mreference'):
			from .Mreference import Mreference
			self._mreference = Mreference(self._core, self._cmd_group)
		return self._mreference

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
		"""x commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_x'):
			from .X import X
			self._x = X(self._core, self._cmd_group)
		return self._x

	@property
	def y(self):
		"""y commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_y'):
			from .Y import Y
			self._y = Y(self._core, self._cmd_group)
		return self._y

	@property
	def spectrogram(self):
		"""spectrogram commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_spectrogram'):
			from .Spectrogram import Spectrogram
			self._spectrogram = Spectrogram(self._core, self._cmd_group)
		return self._spectrogram

	def clone(self) -> 'DeltaMarker':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DeltaMarker(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
