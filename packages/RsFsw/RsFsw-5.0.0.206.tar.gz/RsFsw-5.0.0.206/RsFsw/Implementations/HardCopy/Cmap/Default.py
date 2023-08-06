from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Default:
	"""Default commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: Colors, default value after init: Colors.Ix1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("default", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_colors_get', 'repcap_colors_set', repcap.Colors.Ix1)

	def repcap_colors_set(self, colors: repcap.Colors) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Colors.Default
		Default value after init: Colors.Ix1"""
		self._cmd_group.set_repcap_enum_value(colors)

	def repcap_colors_get(self) -> repcap.Colors:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, item=repcap.Item.Default, colors=repcap.Colors.Default) -> None:
		"""SCPI: HCOPy:CMAP<it>:DEFault<ci> \n
		Snippet: driver.hardCopy.cmap.default.set(item = repcap.Item.Default, colors = repcap.Colors.Default) \n
		This command defines the color scheme for print jobs. For details see 'Print Colors'. \n
			:param item: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Cmap')
			:param colors: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Default')
		"""
		item_cmd_val = self._cmd_group.get_repcap_cmd_value(item, repcap.Item)
		colors_cmd_val = self._cmd_group.get_repcap_cmd_value(colors, repcap.Colors)
		self._core.io.write(f'HCOPy:CMAP{item_cmd_val}:DEFault{colors_cmd_val}')

	def set_with_opc(self, item=repcap.Item.Default, colors=repcap.Colors.Default, opc_timeout_ms: int = -1) -> None:
		item_cmd_val = self._cmd_group.get_repcap_cmd_value(item, repcap.Item)
		colors_cmd_val = self._cmd_group.get_repcap_cmd_value(colors, repcap.Colors)
		"""SCPI: HCOPy:CMAP<it>:DEFault<ci> \n
		Snippet: driver.hardCopy.cmap.default.set_with_opc(item = repcap.Item.Default, colors = repcap.Colors.Default) \n
		This command defines the color scheme for print jobs. For details see 'Print Colors'. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param item: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Cmap')
			:param colors: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Default')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'HCOPy:CMAP{item_cmd_val}:DEFault{colors_cmd_val}', opc_timeout_ms)

	def clone(self) -> 'Default':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Default(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
