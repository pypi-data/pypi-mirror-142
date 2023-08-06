from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPy:
	"""FilterPy commands group definition. 3 total commands, 2 Subgroups, 1 group commands
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
	def name(self):
		"""name commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_name'):
			from .Name import Name
			self._name = Name(self._core, self._cmd_group)
		return self._name

	@property
	def set(self):
		"""set commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_set'):
			from .Set import Set
			self._set = Set(self._core, self._cmd_group)
		return self._set

	def delete(self, filterPy=repcap.FilterPy.Default) -> None:
		"""SCPI: [SENSe]:EVALuation:FILTer<n>:DELete \n
		Snippet: driver.applications.k149Uwb.sense.evaluation.filterPy.delete(filterPy = repcap.FilterPy.Default) \n
		Deletes the specified packet filter. \n
			:param filterPy: optional repeated capability selector. Default value: Nr1 (settable in the interface 'FilterPy')
		"""
		filterPy_cmd_val = self._cmd_group.get_repcap_cmd_value(filterPy, repcap.FilterPy)
		self._core.io.write(f'SENSe:EVALuation:FILTer{filterPy_cmd_val}:DELete')

	def delete_with_opc(self, filterPy=repcap.FilterPy.Default, opc_timeout_ms: int = -1) -> None:
		filterPy_cmd_val = self._cmd_group.get_repcap_cmd_value(filterPy, repcap.FilterPy)
		"""SCPI: [SENSe]:EVALuation:FILTer<n>:DELete \n
		Snippet: driver.applications.k149Uwb.sense.evaluation.filterPy.delete_with_opc(filterPy = repcap.FilterPy.Default) \n
		Deletes the specified packet filter. \n
		Same as delete, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param filterPy: optional repeated capability selector. Default value: Nr1 (settable in the interface 'FilterPy')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:EVALuation:FILTer{filterPy_cmd_val}:DELete', opc_timeout_ms)

	def clone(self) -> 'FilterPy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FilterPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
