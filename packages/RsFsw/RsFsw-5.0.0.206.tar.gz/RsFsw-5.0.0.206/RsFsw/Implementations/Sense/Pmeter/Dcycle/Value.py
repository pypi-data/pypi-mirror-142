from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, percentage: float, powerMeter=repcap.PowerMeter.Default) -> None:
		"""SCPI: [SENSe]:PMETer<p>:DCYCle:VALue \n
		Snippet: driver.sense.pmeter.dcycle.value.set(percentage = 1.0, powerMeter = repcap.PowerMeter.Default) \n
		This command defines the duty cycle for the correction of pulse signals. The power sensor uses the duty cycle in
		combination with the mean power to calculate the power of the pulse. \n
			:param percentage: Range: 0.001 to 99.999, Unit: %
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
		"""
		param = Conversions.decimal_value_to_str(percentage)
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		self._core.io.write(f'SENSe:PMETer{powerMeter_cmd_val}:DCYCle:VALue {param}')

	def get(self, powerMeter=repcap.PowerMeter.Default) -> float:
		"""SCPI: [SENSe]:PMETer<p>:DCYCle:VALue \n
		Snippet: value: float = driver.sense.pmeter.dcycle.value.get(powerMeter = repcap.PowerMeter.Default) \n
		This command defines the duty cycle for the correction of pulse signals. The power sensor uses the duty cycle in
		combination with the mean power to calculate the power of the pulse. \n
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
			:return: percentage: Range: 0.001 to 99.999, Unit: %"""
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		response = self._core.io.query_str(f'SENSe:PMETer{powerMeter_cmd_val}:DCYCle:VALue?')
		return Conversions.str_to_float(response)
