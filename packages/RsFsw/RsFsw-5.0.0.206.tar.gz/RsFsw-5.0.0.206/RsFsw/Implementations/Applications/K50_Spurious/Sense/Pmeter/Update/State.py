from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, arg_0: bool, powerMeter=repcap.PowerMeter.Default) -> None:
		"""SCPI: [SENSe]:PMETer<p>:UPDate[:STATe] \n
		Snippet: driver.applications.k50Spurious.sense.pmeter.update.state.set(arg_0 = False, powerMeter = repcap.PowerMeter.Default) \n
		This command turns continuous update of power sensor measurements on and off. If on, the results are update even if a
		single sweep is complete. \n
			:param arg_0: No help available
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
		"""
		param = Conversions.bool_to_str(arg_0)
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		self._core.io.write(f'SENSe:PMETer{powerMeter_cmd_val}:UPDate:STATe {param}')

	def get(self, powerMeter=repcap.PowerMeter.Default) -> bool:
		"""SCPI: [SENSe]:PMETer<p>:UPDate[:STATe] \n
		Snippet: value: bool = driver.applications.k50Spurious.sense.pmeter.update.state.get(powerMeter = repcap.PowerMeter.Default) \n
		This command turns continuous update of power sensor measurements on and off. If on, the results are update even if a
		single sweep is complete. \n
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
			:return: arg_0: No help available"""
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		response = self._core.io.query_str(f'SENSe:PMETer{powerMeter_cmd_val}:UPDate:STATe?')
		return Conversions.str_to_bool(response)
