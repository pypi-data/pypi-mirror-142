from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Immediate:
	"""Immediate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("immediate", core, parent)

	def set(self, outputConnector=repcap.OutputConnector.Default, triggerPort=repcap.TriggerPort.Default) -> None:
		"""SCPI: OUTPut<up>:TRIGger<tp>:PULSe:IMMediate \n
		Snippet: driver.applications.k70Vsa.output.trigger.pulse.immediate.set(outputConnector = repcap.OutputConnector.Default, triggerPort = repcap.TriggerPort.Default) \n
		This command generates a pulse at the trigger output. \n
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		self._core.io.write(f'OUTPut{outputConnector_cmd_val}:TRIGger{triggerPort_cmd_val}:PULSe:IMMediate')

	def set_with_opc(self, outputConnector=repcap.OutputConnector.Default, triggerPort=repcap.TriggerPort.Default, opc_timeout_ms: int = -1) -> None:
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		"""SCPI: OUTPut<up>:TRIGger<tp>:PULSe:IMMediate \n
		Snippet: driver.applications.k70Vsa.output.trigger.pulse.immediate.set_with_opc(outputConnector = repcap.OutputConnector.Default, triggerPort = repcap.TriggerPort.Default) \n
		This command generates a pulse at the trigger output. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'OUTPut{outputConnector_cmd_val}:TRIGger{triggerPort_cmd_val}:PULSe:IMMediate', opc_timeout_ms)
