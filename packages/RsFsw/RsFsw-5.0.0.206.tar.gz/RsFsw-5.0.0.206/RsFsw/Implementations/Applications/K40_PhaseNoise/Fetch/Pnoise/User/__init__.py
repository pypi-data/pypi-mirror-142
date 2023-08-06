from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class User:
	"""User commands group definition. 4 total commands, 4 Subgroups, 0 group commands
	Repeated Capability: UserRange, default value after init: UserRange.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("user", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_userRange_get', 'repcap_userRange_set', repcap.UserRange.Nr1)

	def repcap_userRange_set(self, userRange: repcap.UserRange) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to UserRange.Default
		Default value after init: UserRange.Nr1"""
		self._cmd_group.set_repcap_enum_value(userRange)

	def repcap_userRange_get(self) -> repcap.UserRange:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

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

	def clone(self) -> 'User':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = User(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
