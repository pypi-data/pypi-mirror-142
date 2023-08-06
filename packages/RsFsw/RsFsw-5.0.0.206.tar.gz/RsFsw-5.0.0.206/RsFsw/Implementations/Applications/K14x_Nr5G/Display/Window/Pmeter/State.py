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

	def set(self, state: bool, window=repcap.Window.Default, powerMeter=repcap.PowerMeter.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:PMETer<p>:STATe \n
		Snippet: driver.applications.k14Xnr5G.display.window.pmeter.state.set(state = False, window = repcap.Window.Default, powerMeter = repcap.PowerMeter.Default) \n
		No command help available \n
			:param state: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:PMETer{powerMeter_cmd_val}:STATe {param}')

	def get(self, window=repcap.Window.Default, powerMeter=repcap.PowerMeter.Default) -> bool:
		"""SCPI: DISPlay[:WINDow<n>]:PMETer<p>:STATe \n
		Snippet: value: bool = driver.applications.k14Xnr5G.display.window.pmeter.state.get(window = repcap.Window.Default, powerMeter = repcap.PowerMeter.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
			:return: state: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:PMETer{powerMeter_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
