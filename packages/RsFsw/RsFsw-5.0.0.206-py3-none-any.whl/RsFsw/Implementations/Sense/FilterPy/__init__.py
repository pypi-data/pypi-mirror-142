from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPy:
	"""FilterPy commands group definition. 13 total commands, 6 Subgroups, 0 group commands
	Repeated Capability: FilterPy, default value after init: FilterPy.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("filterPy", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_filterPy_get', 'repcap_filterPy_set', repcap.FilterPy.Nr1)

	def repcap_filterPy_set(self, filterPy: repcap.FilterPy) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to FilterPy.Default
		Default value after init: FilterPy.Nr1"""
		self._cmd_group.set_repcap_enum_value(filterPy)

	def repcap_filterPy_get(self) -> repcap.FilterPy:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def hpass(self):
		"""hpass commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_hpass'):
			from .Hpass import Hpass
			self._hpass = Hpass(self._core, self._cmd_group)
		return self._hpass

	@property
	def lpass(self):
		"""lpass commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_lpass'):
			from .Lpass import Lpass
			self._lpass = Lpass(self._core, self._cmd_group)
		return self._lpass

	@property
	def demphasis(self):
		"""demphasis commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_demphasis'):
			from .Demphasis import Demphasis
			self._demphasis = Demphasis(self._core, self._cmd_group)
		return self._demphasis

	@property
	def ccir(self):
		"""ccir commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ccir'):
			from .Ccir import Ccir
			self._ccir = Ccir(self._core, self._cmd_group)
		return self._ccir

	@property
	def aweighted(self):
		"""aweighted commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_aweighted'):
			from .Aweighted import Aweighted
			self._aweighted = Aweighted(self._core, self._cmd_group)
		return self._aweighted

	@property
	def aoff(self):
		"""aoff commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aoff'):
			from .Aoff import Aoff
			self._aoff = Aoff(self._core, self._cmd_group)
		return self._aoff

	def clone(self) -> 'FilterPy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FilterPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
