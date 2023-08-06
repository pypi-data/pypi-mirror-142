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

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:TRENd:LLINes[:STATe] \n
		Snippet: driver.applications.k6Pulse.calculate.trend.llines.state.set(state = False, window = repcap.Window.Default) \n
		Hides or shows the limit lines in the selected Parameter Trend or Parameter Distribution result display. Note that this
		function only has an effect on the visibility of the lines in the graphical displays, it does not affect the limit check
		in general or the display of the limit check results in the table displays. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:TRENd:LLINes:STATe {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: CALCulate<n>:TRENd:LLINes[:STATe] \n
		Snippet: value: bool = driver.applications.k6Pulse.calculate.trend.llines.state.get(window = repcap.Window.Default) \n
		Hides or shows the limit lines in the selected Parameter Trend or Parameter Distribution result display. Note that this
		function only has an effect on the visibility of the lines in the graphical displays, it does not affect the limit check
		in general or the display of the limit check results in the table displays. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:TRENd:LLINes:STATe?')
		return Conversions.str_to_bool(response)
