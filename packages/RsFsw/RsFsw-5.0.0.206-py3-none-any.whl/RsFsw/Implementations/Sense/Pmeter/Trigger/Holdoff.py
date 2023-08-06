from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Holdoff:
	"""Holdoff commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("holdoff", core, parent)

	def set(self, holdoff: float, powerMeter=repcap.PowerMeter.Default) -> None:
		"""SCPI: [SENSe]:PMETer<p>:TRIGger:HOLDoff \n
		Snippet: driver.sense.pmeter.trigger.holdoff.set(holdoff = 1.0, powerMeter = repcap.PowerMeter.Default) \n
		This command defines the trigger holdoff for external power triggers. \n
			:param holdoff: Time period that has to pass between the trigger event and the start of the measurement, in case another trigger event occurs. Range: 0 s to 1 s, Unit: S
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
		"""
		param = Conversions.decimal_value_to_str(holdoff)
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		self._core.io.write(f'SENSe:PMETer{powerMeter_cmd_val}:TRIGger:HOLDoff {param}')

	def get(self, powerMeter=repcap.PowerMeter.Default) -> float:
		"""SCPI: [SENSe]:PMETer<p>:TRIGger:HOLDoff \n
		Snippet: value: float = driver.sense.pmeter.trigger.holdoff.get(powerMeter = repcap.PowerMeter.Default) \n
		This command defines the trigger holdoff for external power triggers. \n
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
			:return: holdoff: Time period that has to pass between the trigger event and the start of the measurement, in case another trigger event occurs. Range: 0 s to 1 s, Unit: S"""
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		response = self._core.io.query_str(f'SENSe:PMETer{powerMeter_cmd_val}:TRIGger:HOLDoff?')
		return Conversions.str_to_float(response)
