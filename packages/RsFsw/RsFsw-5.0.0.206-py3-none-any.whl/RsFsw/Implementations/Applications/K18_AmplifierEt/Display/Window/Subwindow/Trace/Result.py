from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Result:
	"""Result commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("result", core, parent)

	def set(self, trace_result: enums.TraceResultK18, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:TRACe<t>:RESult \n
		Snippet: driver.applications.k18AmplifierEt.display.window.subwindow.trace.result.set(trace_result = enums.TraceResultK18.BBI, window = repcap.Window.Default, subWindow = repcap.SubWindow.Default, trace = repcap.Trace.Default) \n
		Sets and queries the trace result type for the selected result display. \n
			:param trace_result: BBI | BBPower | BBQ | RF | MEAS | MODel | REFerence
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.enum_scalar_to_str(trace_result, enums.TraceResultK18)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:TRACe{trace_cmd_val}:RESult {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default, trace=repcap.Trace.Default) -> enums.TraceResultK18:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:TRACe<t>:RESult \n
		Snippet: value: enums.TraceResultK18 = driver.applications.k18AmplifierEt.display.window.subwindow.trace.result.get(window = repcap.Window.Default, subWindow = repcap.SubWindow.Default, trace = repcap.Trace.Default) \n
		Sets and queries the trace result type for the selected result display. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: trace_result: BBI | BBPower | BBQ | RF | MEAS | MODel | REFerence"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:TRACe{trace_cmd_val}:RESult?')
		return Conversions.str_to_scalar_enum(response, enums.TraceResultK18)
