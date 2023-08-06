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

	def set(self, state: bool, powerMeter=repcap.PowerMeter.Default) -> None:
		"""SCPI: [SENSe]:PMETer<p>:DCYCle[:STATe] \n
		Snippet: driver.applications.k14Xnr5G.sense.pmeter.dcycle.state.set(state = False, powerMeter = repcap.PowerMeter.Default) \n
		No command help available \n
			:param state: No help available
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
		"""
		param = Conversions.bool_to_str(state)
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		self._core.io.write(f'SENSe:PMETer{powerMeter_cmd_val}:DCYCle:STATe {param}')

	def get(self, powerMeter=repcap.PowerMeter.Default) -> bool:
		"""SCPI: [SENSe]:PMETer<p>:DCYCle[:STATe] \n
		Snippet: value: bool = driver.applications.k14Xnr5G.sense.pmeter.dcycle.state.get(powerMeter = repcap.PowerMeter.Default) \n
		No command help available \n
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
			:return: state: No help available"""
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		response = self._core.io.query_str(f'SENSe:PMETer{powerMeter_cmd_val}:DCYCle:STATe?')
		return Conversions.str_to_bool(response)
