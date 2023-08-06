from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Immediate:
	"""Immediate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("immediate", core, parent)

	def set(self, triggerPort=repcap.TriggerPort.Default) -> None:
		"""SCPI: OUTPut:TRIGger<2|3>:PULSe:IMMediate \n
		Snippet: driver.output.trigger.pulse.immediate.set(triggerPort = repcap.TriggerPort.Default) \n
		This command generates a pulse at the trigger output. \n
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		self._core.io.write(f'OUTPut:TRIGger{triggerPort_cmd_val}:PULSe:IMMediate')

	def set_with_opc(self, triggerPort=repcap.TriggerPort.Default, opc_timeout_ms: int = -1) -> None:
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		"""SCPI: OUTPut:TRIGger<2|3>:PULSe:IMMediate \n
		Snippet: driver.output.trigger.pulse.immediate.set_with_opc(triggerPort = repcap.TriggerPort.Default) \n
		This command generates a pulse at the trigger output. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'OUTPut:TRIGger{triggerPort_cmd_val}:PULSe:IMMediate', opc_timeout_ms)
