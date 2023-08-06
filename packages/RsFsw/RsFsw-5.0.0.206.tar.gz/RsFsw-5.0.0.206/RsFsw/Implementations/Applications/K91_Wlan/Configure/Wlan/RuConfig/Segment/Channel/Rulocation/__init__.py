from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal.RepeatedCapability import RepeatedCapability
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rulocation:
	"""Rulocation commands group definition. 14 total commands, 7 Subgroups, 0 group commands
	Repeated Capability: RuAllocationIx, default value after init: RuAllocationIx.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rulocation", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_ruAllocationIx_get', 'repcap_ruAllocationIx_set', repcap.RuAllocationIx.Nr1)

	def repcap_ruAllocationIx_set(self, ruAllocationIx: repcap.RuAllocationIx) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to RuAllocationIx.Default
		Default value after init: RuAllocationIx.Nr1"""
		self._cmd_group.set_repcap_enum_value(ruAllocationIx)

	def repcap_ruAllocationIx_get(self) -> repcap.RuAllocationIx:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def ru26Index(self):
		"""ru26Index commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ru26Index'):
			from .Ru26Index import Ru26Index
			self._ru26Index = Ru26Index(self._core, self._cmd_group)
		return self._ru26Index

	@property
	def rutSix(self):
		"""rutSix commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rutSix'):
			from .RutSix import RutSix
			self._rutSix = RutSix(self._core, self._cmd_group)
		return self._rutSix

	@property
	def ruIndex(self):
		"""ruIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ruIndex'):
			from .RuIndex import RuIndex
			self._ruIndex = RuIndex(self._core, self._cmd_group)
		return self._ruIndex

	@property
	def count(self):
		"""count commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_count'):
			from .Count import Count
			self._count = Count(self._core, self._cmd_group)
		return self._count

	@property
	def user(self):
		"""user commands group. 7 Sub-classes, 1 commands."""
		if not hasattr(self, '_user'):
			from .User import User
			self._user = User(self._core, self._cmd_group)
		return self._user

	@property
	def ruSize(self):
		"""ruSize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ruSize'):
			from .RuSize import RuSize
			self._ruSize = RuSize(self._core, self._cmd_group)
		return self._ruSize

	@property
	def mruIndex(self):
		"""mruIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mruIndex'):
			from .MruIndex import MruIndex
			self._mruIndex = MruIndex(self._core, self._cmd_group)
		return self._mruIndex

	def clone(self) -> 'Rulocation':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rulocation(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
