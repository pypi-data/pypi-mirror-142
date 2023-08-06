from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aperture:
	"""Aperture commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aperture", core, parent)

	def set(self, aperture: float, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:TRACe<t>:SMOothing:APERture \n
		Snippet: driver.display.window.subwindow.trace.smoothing.aperture.set(aperture = 1.0, window = repcap.Window.Default, subWindow = repcap.SubWindow.Default, trace = repcap.Trace.Default) \n
		This command defines the degree (aperture) of the trace smoothing, if method RsFsw.Display.Window.Subwindow.Trace.
		Smoothing.State.setTRUE. \n
			:param aperture: Range: 1 to 50, Unit: PCT
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.decimal_value_to_str(aperture)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:TRACe{trace_cmd_val}:SMOothing:APERture {param}')

	def get(self, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default, trace=repcap.Trace.Default) -> float:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:TRACe<t>:SMOothing:APERture \n
		Snippet: value: float = driver.display.window.subwindow.trace.smoothing.aperture.get(window = repcap.Window.Default, subWindow = repcap.SubWindow.Default, trace = repcap.Trace.Default) \n
		This command defines the degree (aperture) of the trace smoothing, if method RsFsw.Display.Window.Subwindow.Trace.
		Smoothing.State.setTRUE. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: aperture: Range: 1 to 50, Unit: PCT"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:TRACe{trace_cmd_val}:SMOothing:APERture?')
		return Conversions.str_to_float(response)
