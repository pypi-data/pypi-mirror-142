from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Holdoff:
	"""Holdoff commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("holdoff", core, parent)

	def set(self, time: float, triggerPort=repcap.TriggerPort.Default) -> None:
		"""SCPI: TRIGger<tp>[:SEQuence]:RFPower:HOLDoff \n
		Snippet: driver.applications.k70Vsa.trigger.sequence.rfPower.holdoff.set(time = 1.0, triggerPort = repcap.TriggerPort.Default) \n
		No command help available \n
			:param time: No help available
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		param = Conversions.decimal_value_to_str(time)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		self._core.io.write(f'TRIGger{triggerPort_cmd_val}:SEQuence:RFPower:HOLDoff {param}')

	def get(self, triggerPort=repcap.TriggerPort.Default) -> float:
		"""SCPI: TRIGger<tp>[:SEQuence]:RFPower:HOLDoff \n
		Snippet: value: float = driver.applications.k70Vsa.trigger.sequence.rfPower.holdoff.get(triggerPort = repcap.TriggerPort.Default) \n
		No command help available \n
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:return: time: No help available"""
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		response = self._core.io.query_str(f'TRIGger{triggerPort_cmd_val}:SEQuence:RFPower:HOLDoff?')
		return Conversions.str_to_float(response)
