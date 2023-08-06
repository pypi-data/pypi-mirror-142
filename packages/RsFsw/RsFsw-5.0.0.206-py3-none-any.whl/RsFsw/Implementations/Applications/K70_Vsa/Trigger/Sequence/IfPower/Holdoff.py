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

	def set(self, period: float, triggerPort=repcap.TriggerPort.Default) -> None:
		"""SCPI: TRIGger<tp>[:SEQuence]:IFPower:HOLDoff \n
		Snippet: driver.applications.k70Vsa.trigger.sequence.ifPower.holdoff.set(period = 1.0, triggerPort = repcap.TriggerPort.Default) \n
		This command defines the holding time before the next trigger event. Note that this command can be used for any trigger
		source, not just IF Power (despite the legacy keyword) . Note: If you perform gated measurements in combination with the
		IF Power trigger, the R&S FSW ignores the holding time for frequency sweep, FFT sweep, zero span and I/Q data
		measurements. \n
			:param period: Range: 0 s to 10 s, Unit: S
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
		"""
		param = Conversions.decimal_value_to_str(period)
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		self._core.io.write(f'TRIGger{triggerPort_cmd_val}:SEQuence:IFPower:HOLDoff {param}')

	def get(self, triggerPort=repcap.TriggerPort.Default) -> float:
		"""SCPI: TRIGger<tp>[:SEQuence]:IFPower:HOLDoff \n
		Snippet: value: float = driver.applications.k70Vsa.trigger.sequence.ifPower.holdoff.get(triggerPort = repcap.TriggerPort.Default) \n
		This command defines the holding time before the next trigger event. Note that this command can be used for any trigger
		source, not just IF Power (despite the legacy keyword) . Note: If you perform gated measurements in combination with the
		IF Power trigger, the R&S FSW ignores the holding time for frequency sweep, FFT sweep, zero span and I/Q data
		measurements. \n
			:param triggerPort: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trigger')
			:return: period: Range: 0 s to 10 s, Unit: S"""
		triggerPort_cmd_val = self._cmd_group.get_repcap_cmd_value(triggerPort, repcap.TriggerPort)
		response = self._core.io.query_str(f'TRIGger{triggerPort_cmd_val}:SEQuence:IFPower:HOLDoff?')
		return Conversions.str_to_float(response)
