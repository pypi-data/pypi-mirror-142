from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rinterval:
	"""Rinterval commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rinterval", core, parent)

	def set(self, interval: float, triggerPort=repcap.TriggerPort.Default) -> None:
		"""SCPI: TRIGger<tp>[:SEQuence]:TIME:RINTerval \n
		Snippet: driver.applications.k70Vsa.trigger.sequence.time.rinterval.set(interval = 1.0, triggerPort = repcap.TriggerPort.Default) \n
		This command defines the repetition interval for the time trigger. \n
			:param interval: 2.0 ms to 5000 Range: 2 ns to 5000 s, Unit: S
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		param = Conversions.decimal_value_to_str(interval)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		self._core.io.write(f'TRIGger{triggerPort_cmd_val}:SEQuence:TIME:RINTerval {param}')

	def get(self, triggerPort=repcap.TriggerPort.Default) -> float:
		"""SCPI: TRIGger<tp>[:SEQuence]:TIME:RINTerval \n
		Snippet: value: float = driver.applications.k70Vsa.trigger.sequence.time.rinterval.get(triggerPort = repcap.TriggerPort.Default) \n
		This command defines the repetition interval for the time trigger. \n
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:return: interval: 2.0 ms to 5000 Range: 2 ns to 5000 s, Unit: S"""
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		response = self._core.io.query_str(f'TRIGger{triggerPort_cmd_val}:SEQuence:TIME:RINTerval?')
		return Conversions.str_to_float(response)
