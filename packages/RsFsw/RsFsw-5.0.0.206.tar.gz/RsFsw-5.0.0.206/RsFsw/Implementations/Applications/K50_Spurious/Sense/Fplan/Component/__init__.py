from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Component:
	"""Component commands group definition. 9 total commands, 7 Subgroups, 1 group commands
	Repeated Capability: Component, default value after init: Component.Ix1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("component", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_component_get', 'repcap_component_set', repcap.Component.Ix1)

	def repcap_component_set(self, component: repcap.Component) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Component.Default
		Default value after init: Component.Ix1"""
		self._cmd_group.set_repcap_enum_value(component)

	def repcap_component_get(self) -> repcap.Component:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePy
			self._typePy = TypePy(self._core, self._cmd_group)
		return self._typePy

	@property
	def bcenter(self):
		"""bcenter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bcenter'):
			from .Bcenter import Bcenter
			self._bcenter = Bcenter(self._core, self._cmd_group)
		return self._bcenter

	@property
	def bspan(self):
		"""bspan commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bspan'):
			from .Bspan import Bspan
			self._bspan = Bspan(self._core, self._cmd_group)
		return self._bspan

	@property
	def add(self):
		"""add commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_add'):
			from .Add import Add
			self._add = Add(self._core, self._cmd_group)
		return self._add

	@property
	def factor(self):
		"""factor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_factor'):
			from .Factor import Factor
			self._factor = Factor(self._core, self._cmd_group)
		return self._factor

	@property
	def port(self):
		"""port commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_port'):
			from .Port import Port
			self._port = Port(self._core, self._cmd_group)
		return self._port

	@property
	def identity(self):
		"""identity commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_identity'):
			from .Identity import Identity
			self._identity = Identity(self._core, self._cmd_group)
		return self._identity

	def delete(self, component=repcap.Component.Default) -> None:
		"""SCPI: [SENSe]:FPLan:COMPonent<co>:DELete \n
		Snippet: driver.applications.k50Spurious.sense.fplan.component.delete(component = repcap.Component.Default) \n
		This command will delete the selected row from the frequency plan. \n
			:param component: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Component')
		"""
		component_cmd_val = self._cmd_group.get_repcap_cmd_value(component, repcap.Component)
		self._core.io.write(f'SENSe:FPLan:COMPonent{component_cmd_val}:DELete')

	def delete_with_opc(self, component=repcap.Component.Default, opc_timeout_ms: int = -1) -> None:
		component_cmd_val = self._cmd_group.get_repcap_cmd_value(component, repcap.Component)
		"""SCPI: [SENSe]:FPLan:COMPonent<co>:DELete \n
		Snippet: driver.applications.k50Spurious.sense.fplan.component.delete_with_opc(component = repcap.Component.Default) \n
		This command will delete the selected row from the frequency plan. \n
		Same as delete, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param component: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Component')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:FPLan:COMPonent{component_cmd_val}:DELete', opc_timeout_ms)

	def clone(self) -> 'Component':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Component(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
