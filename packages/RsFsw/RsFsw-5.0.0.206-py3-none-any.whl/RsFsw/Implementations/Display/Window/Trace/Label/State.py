from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:LABel[:STATe] \n
		Snippet: driver.display.window.trace.label.state.set(state = False, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		Turns on the display of a descriptive label for the specified trace instead of the default 'Trace <x>' label. Define the
		label using the method RsFsw.Display.Window.Trace.Label.Text.set command. You can only configure labels for active traces
		and for traces whose 'State' is enabled. \n
			:param state: OFF Switch the function off ON Switch the function on
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:LABel:STATe {param}')

	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> bool:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:LABel[:STATe] \n
		Snippet: value: bool = driver.display.window.trace.label.state.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		Turns on the display of a descriptive label for the specified trace instead of the default 'Trace <x>' label. Define the
		label using the method RsFsw.Display.Window.Trace.Label.Text.set command. You can only configure labels for active traces
		and for traces whose 'State' is enabled. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: state: OFF Switch the function off ON Switch the function on"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:LABel:STATe?')
		return Conversions.str_to_bool(response)
