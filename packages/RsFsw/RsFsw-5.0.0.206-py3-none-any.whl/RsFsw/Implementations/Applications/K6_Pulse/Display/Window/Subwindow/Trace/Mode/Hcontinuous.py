from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hcontinuous:
	"""Hcontinuous commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hcontinuous", core, parent)

	def set(self, hcontinuous: bool, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:TRACe<t>:MODE:HCONtinuous \n
		Snippet: driver.applications.k6Pulse.display.window.subwindow.trace.mode.hcontinuous.set(hcontinuous = False, window = repcap.Window.Default, subWindow = repcap.SubWindow.Default, trace = repcap.Trace.Default) \n
		This command turns an automatic reset of a trace on and off after a parameter has changed. The reset works for trace
		modes min hold, max hold and average. Note that the command has no effect if critical parameters like the span have been
		changed to avoid invalid measurement results \n
			:param hcontinuous: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.bool_to_str(hcontinuous)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:TRACe{trace_cmd_val}:MODE:HCONtinuous {param}')

	def get(self, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default, trace=repcap.Trace.Default) -> bool:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:TRACe<t>:MODE:HCONtinuous \n
		Snippet: value: bool = driver.applications.k6Pulse.display.window.subwindow.trace.mode.hcontinuous.get(window = repcap.Window.Default, subWindow = repcap.SubWindow.Default, trace = repcap.Trace.Default) \n
		This command turns an automatic reset of a trace on and off after a parameter has changed. The reset works for trace
		modes min hold, max hold and average. Note that the command has no effect if critical parameters like the span have been
		changed to avoid invalid measurement results \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: hcontinuous: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:TRACe{trace_cmd_val}:MODE:HCONtinuous?')
		return Conversions.str_to_bool(response)
