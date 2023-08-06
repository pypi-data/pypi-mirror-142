from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pnoise:
	"""Pnoise commands group definition. 20 total commands, 8 Subgroups, 0 group commands
	Repeated Capability: Trace, default value after init: Trace.Tr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pnoise", core, parent)
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
	def spurs(self):
		"""spurs commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_spurs'):
			from .Spurs import Spurs
			self._spurs = Spurs(self._core, self._cmd_group)
		return self._spurs

	@property
	def measured(self):
		"""measured commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_measured'):
			from .Measured import Measured
			self._measured = Measured(self._core, self._cmd_group)
		return self._measured

	@property
	def sweep(self):
		"""sweep commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_sweep'):
			from .Sweep import Sweep
			self._sweep = Sweep(self._core, self._cmd_group)
		return self._sweep

	@property
	def ipn(self):
		"""ipn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ipn'):
			from .Ipn import Ipn
			self._ipn = Ipn(self._core, self._cmd_group)
		return self._ipn

	@property
	def rfm(self):
		"""rfm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rfm'):
			from .Rfm import Rfm
			self._rfm = Rfm(self._core, self._cmd_group)
		return self._rfm

	@property
	def rms(self):
		"""rms commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rms'):
			from .Rms import Rms
			self._rms = Rms(self._core, self._cmd_group)
		return self._rms

	@property
	def rpm(self):
		"""rpm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rpm'):
			from .Rpm import Rpm
			self._rpm = Rpm(self._core, self._cmd_group)
		return self._rpm

	@property
	def user(self):
		"""user commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_user'):
			from .User import User
			self._user = User(self._core, self._cmd_group)
		return self._user

	def clone(self) -> 'Pnoise':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pnoise(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
