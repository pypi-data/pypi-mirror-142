from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, powerMeter=repcap.PowerMeter.Default) -> None:
		"""SCPI: SYSTem:COMMunicate:RDEVice:PMETer<p>:CONFigure:AUTO[:STATe] \n
		Snippet: driver.system.communicate.rdevice.pmeter.configure.auto.state.set(state = False, powerMeter = repcap.PowerMeter.Default) \n
		This command turns automatic assignment of a power sensor to the power sensor index on and off. \n
			:param state: ON | OFF | 0 | 1
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
		"""
		param = Conversions.bool_to_str(state)
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		self._core.io.write(f'SYSTem:COMMunicate:RDEVice:PMETer{powerMeter_cmd_val}:CONFigure:AUTO:STATe {param}')

	def get(self, powerMeter=repcap.PowerMeter.Default) -> bool:
		"""SCPI: SYSTem:COMMunicate:RDEVice:PMETer<p>:CONFigure:AUTO[:STATe] \n
		Snippet: value: bool = driver.system.communicate.rdevice.pmeter.configure.auto.state.get(powerMeter = repcap.PowerMeter.Default) \n
		This command turns automatic assignment of a power sensor to the power sensor index on and off. \n
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
			:return: state: ON | OFF | 0 | 1"""
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		response = self._core.io.query_str(f'SYSTem:COMMunicate:RDEVice:PMETer{powerMeter_cmd_val}:CONFigure:AUTO:STATe?')
		return Conversions.str_to_bool(response)
