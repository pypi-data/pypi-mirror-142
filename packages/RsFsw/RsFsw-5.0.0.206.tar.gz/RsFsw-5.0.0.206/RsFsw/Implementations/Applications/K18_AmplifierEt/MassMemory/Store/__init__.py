from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Store:
	"""Store commands group definition. 8 total commands, 6 Subgroups, 0 group commands
	Repeated Capability: Store, default value after init: Store.Pos1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("store", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_store_get', 'repcap_store_set', repcap.Store.Pos1)

	def repcap_store_set(self, store: repcap.Store) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Store.Default
		Default value after init: Store.Pos1"""
		self._cmd_group.set_repcap_enum_value(store)

	def repcap_store_get(self) -> repcap.Store:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def dpd(self):
		"""dpd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dpd'):
			from .Dpd import Dpd
			self._dpd = Dpd(self._core, self._cmd_group)
		return self._dpd

	@property
	def ddpd(self):
		"""ddpd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ddpd'):
			from .Ddpd import Ddpd
			self._ddpd = Ddpd(self._core, self._cmd_group)
		return self._ddpd

	@property
	def equalizer(self):
		"""equalizer commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_equalizer'):
			from .Equalizer import Equalizer
			self._equalizer = Equalizer(self._core, self._cmd_group)
		return self._equalizer

	@property
	def mdpd(self):
		"""mdpd commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_mdpd'):
			from .Mdpd import Mdpd
			self._mdpd = Mdpd(self._core, self._cmd_group)
		return self._mdpd

	@property
	def iq(self):
		"""iq commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_iq'):
			from .Iq import Iq
			self._iq = Iq(self._core, self._cmd_group)
		return self._iq

	@property
	def trace(self):
		"""trace commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import Trace
			self._trace = Trace(self._core, self._cmd_group)
		return self._trace

	def clone(self) -> 'Store':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Store(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
