from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hysteresis:
	"""Hysteresis commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hysteresis", core, parent)

	def set(self, hysteresis: float, powerMeter=repcap.PowerMeter.Default) -> None:
		"""SCPI: [SENSe]:PMETer<p>:TRIGger:HYSTeresis \n
		Snippet: driver.applications.k14Xnr5G.sense.pmeter.trigger.hysteresis.set(hysteresis = 1.0, powerMeter = repcap.PowerMeter.Default) \n
		No command help available \n
			:param hysteresis: No help available
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
		"""
		param = Conversions.decimal_value_to_str(hysteresis)
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		self._core.io.write(f'SENSe:PMETer{powerMeter_cmd_val}:TRIGger:HYSTeresis {param}')

	def get(self, powerMeter=repcap.PowerMeter.Default) -> float:
		"""SCPI: [SENSe]:PMETer<p>:TRIGger:HYSTeresis \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.pmeter.trigger.hysteresis.get(powerMeter = repcap.PowerMeter.Default) \n
		No command help available \n
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
			:return: hysteresis: No help available"""
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		response = self._core.io.query_str(f'SENSe:PMETer{powerMeter_cmd_val}:TRIGger:HYSTeresis?')
		return Conversions.str_to_float(response)
