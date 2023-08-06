from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Text:
	"""Text commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("text", core, parent)

	def set(self, text: str, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:LABel:TEXT \n
		Snippet: driver.display.window.trace.label.text.set(text = '1', window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		Defines a descriptive label for the specified trace instead of the default 'Trace <x>' label. Enable the label using the
		method RsFsw.Display.Window.Trace.Label.State.set command. You can only configure labels for active traces and for traces
		whose 'State' is enabled. \n
			:param text: String containing the trace label.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.value_to_quoted_str(text)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:LABel:TEXT {param}')

	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> str:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:LABel:TEXT \n
		Snippet: value: str = driver.display.window.trace.label.text.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		Defines a descriptive label for the specified trace instead of the default 'Trace <x>' label. Enable the label using the
		method RsFsw.Display.Window.Trace.Label.State.set command. You can only configure labels for active traces and for traces
		whose 'State' is enabled. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: text: String containing the trace label."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:LABel:TEXT?')
		return trim_str_response(response)
