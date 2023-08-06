from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Time:
	"""Time commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("time", core, parent)

	def set(self, offset: float, triggerPort=repcap.TriggerPort.Default) -> None:
		"""SCPI: TRIGger<tp>[:SEQuence]:HOLDoff[:TIME] \n
		Snippet: driver.applications.k30NoiseFigure.trigger.sequence.holdoff.time.set(offset = 1.0, triggerPort = repcap.TriggerPort.Default) \n
		Defines the time offset between the trigger event and the start of the sweep. \n
			:param offset: Unit: S
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		param = Conversions.decimal_value_to_str(offset)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		self._core.io.write(f'TRIGger{triggerPort_cmd_val}:SEQuence:HOLDoff:TIME {param}')

	def get(self, triggerPort=repcap.TriggerPort.Default) -> float:
		"""SCPI: TRIGger<tp>[:SEQuence]:HOLDoff[:TIME] \n
		Snippet: value: float = driver.applications.k30NoiseFigure.trigger.sequence.holdoff.time.get(triggerPort = repcap.TriggerPort.Default) \n
		Defines the time offset between the trigger event and the start of the sweep. \n
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:return: offset: Unit: S"""
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		response = self._core.io.query_str(f'TRIGger{triggerPort_cmd_val}:SEQuence:HOLDoff:TIME?')
		return Conversions.str_to_float(response)
