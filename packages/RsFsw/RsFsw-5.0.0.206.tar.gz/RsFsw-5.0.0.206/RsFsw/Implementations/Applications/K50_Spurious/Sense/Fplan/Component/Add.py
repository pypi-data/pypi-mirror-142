from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Add:
	"""Add commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("add", core, parent)

	def set(self, component=repcap.Component.Default) -> None:
		"""SCPI: [SENSe]:FPLan:COMPonent<co>:ADD \n
		Snippet: driver.applications.k50Spurious.sense.fplan.component.add.set(component = repcap.Component.Default) \n
		Adds a new component below the selected row <co> in the frequency plan. If the command is executed on a row that does not
		yet exist, this row and all that are missing up to this row are created. \n
			:param component: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Component')
		"""
		component_cmd_val = self._cmd_group.get_repcap_cmd_value(component, repcap.Component)
		self._core.io.write(f'SENSe:FPLan:COMPonent{component_cmd_val}:ADD')

	def set_with_opc(self, component=repcap.Component.Default, opc_timeout_ms: int = -1) -> None:
		component_cmd_val = self._cmd_group.get_repcap_cmd_value(component, repcap.Component)
		"""SCPI: [SENSe]:FPLan:COMPonent<co>:ADD \n
		Snippet: driver.applications.k50Spurious.sense.fplan.component.add.set_with_opc(component = repcap.Component.Default) \n
		Adds a new component below the selected row <co> in the frequency plan. If the command is executed on a row that does not
		yet exist, this row and all that are missing up to this row are created. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param component: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Component')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:FPLan:COMPonent{component_cmd_val}:ADD', opc_timeout_ms)
