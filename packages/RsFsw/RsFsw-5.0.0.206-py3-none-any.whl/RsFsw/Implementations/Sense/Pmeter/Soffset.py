from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Soffset:
	"""Soffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("soffset", core, parent)

	def set(self, sensor_offset: float, powerMeter=repcap.PowerMeter.Default) -> None:
		"""SCPI: [SENSe]:PMETer<p>:SOFFset \n
		Snippet: driver.sense.pmeter.soffset.set(sensor_offset = 1.0, powerMeter = repcap.PowerMeter.Default) \n
		Takes the specified offset into account for the measured power. Only available if [SENSe:]PMETer{p}:ROFFset[:STATe] is
		disabled. \n
			:param sensor_offset: Unit: DB
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
		"""
		param = Conversions.decimal_value_to_str(sensor_offset)
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		self._core.io.write(f'SENSe:PMETer{powerMeter_cmd_val}:SOFFset {param}')

	def get(self, powerMeter=repcap.PowerMeter.Default) -> float:
		"""SCPI: [SENSe]:PMETer<p>:SOFFset \n
		Snippet: value: float = driver.sense.pmeter.soffset.get(powerMeter = repcap.PowerMeter.Default) \n
		Takes the specified offset into account for the measured power. Only available if [SENSe:]PMETer{p}:ROFFset[:STATe] is
		disabled. \n
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
			:return: sensor_offset: Unit: DB"""
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		response = self._core.io.query_str(f'SENSe:PMETer{powerMeter_cmd_val}:SOFFset?')
		return Conversions.str_to_float(response)
