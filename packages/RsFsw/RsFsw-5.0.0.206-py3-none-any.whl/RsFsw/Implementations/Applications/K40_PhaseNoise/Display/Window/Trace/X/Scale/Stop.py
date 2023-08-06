from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stop:
	"""Stop commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stop", core, parent)

	def set(self, stop_frequency: float, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:X[:SCALe]:STOP \n
		Snippet: driver.applications.k40PhaseNoise.display.window.trace.x.scale.stop.set(stop_frequency = 1.0, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command selects the stop frequency of the display range. Before you can use the command you have to select a manual
		display range for the x-axis with method RsFsw.Applications.K40_PhaseNoise.Display.Window.Trace.X.Scale.Scope.set. \n
			:param stop_frequency: Stop offset frequency of a half decade. Note that the stop offset you want to display has to be part of the current measurement range. Range: 300 mHz to 10 GHz, Unit: HZ
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.decimal_value_to_str(stop_frequency)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:X:SCALe:STOP {param}')

	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> float:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:X[:SCALe]:STOP \n
		Snippet: value: float = driver.applications.k40PhaseNoise.display.window.trace.x.scale.stop.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command selects the stop frequency of the display range. Before you can use the command you have to select a manual
		display range for the x-axis with method RsFsw.Applications.K40_PhaseNoise.Display.Window.Trace.X.Scale.Scope.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: stop_frequency: Stop offset frequency of a half decade. Note that the stop offset you want to display has to be part of the current measurement range. Range: 300 mHz to 10 GHz, Unit: HZ"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:X:SCALe:STOP?')
		return Conversions.str_to_float(response)
