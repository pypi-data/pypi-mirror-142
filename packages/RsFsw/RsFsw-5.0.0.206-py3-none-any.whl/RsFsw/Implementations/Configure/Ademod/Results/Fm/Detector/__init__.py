from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Detector:
	"""Detector commands group definition. 4 total commands, 3 Subgroups, 0 group commands
	Repeated Capability: Trace, default value after init: Trace.Tr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("detector", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_trace_get', 'repcap_trace_set', repcap.Trace.Tr1)

	def repcap_trace_set(self, trace: repcap.Trace) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Trace.Default
		Default value after init: Trace.Tr1"""
		self._cmd_group.set_repcap_enum_value(trace)

	def repcap_trace_get(self) -> repcap.Trace:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def reference(self):
		"""reference commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_reference'):
			from .Reference import Reference
			self._reference = Reference(self._core, self._cmd_group)
		return self._reference

	def clone(self) -> 'Detector':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Detector(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
