from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.TraceModeJ, window=repcap.Window.Default, trace=repcap.Trace.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:MODE \n
		Snippet: driver.applications.k9X11Ad.display.window.trace.mode.set(mode = enums.TraceModeJ.AVER, window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command selects the trace mode. If necessary, the selected trace is also activated. In case of max hold, min hold or
		average trace mode, you can set the number of single measurements with [SENSe:]SWEep:COUNt. Note that synchronization to
		the end of the measurement is possible only in single sweep mode. For more information see 'Analyzing Several Traces -
		Trace Mode'. \n
			:param mode: WRITe Overwrite mode: the trace is overwritten by each sweep. This is the default setting. AVERage The average is formed over several sweeps. The 'Sweep/Average Count' determines the number of averaging procedures. MAXHold The maximum value is determined over several sweeps and displayed. The R&S FSW saves the sweep result in the trace memory only if the new value is greater than the previous one. MINHold The minimum value is determined from several measurements and displayed. The R&S FSW saves the sweep result in the trace memory only if the new value is lower than the previous one. VIEW The current contents of the trace memory are frozen and displayed. BLANk Hides the selected trace.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.TraceModeJ)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, trace=repcap.Trace.Default) -> enums.TraceModeJ:
		"""SCPI: DISPlay[:WINDow<n>]:TRACe<t>:MODE \n
		Snippet: value: enums.TraceModeJ = driver.applications.k9X11Ad.display.window.trace.mode.get(window = repcap.Window.Default, trace = repcap.Trace.Default) \n
		This command selects the trace mode. If necessary, the selected trace is also activated. In case of max hold, min hold or
		average trace mode, you can set the number of single measurements with [SENSe:]SWEep:COUNt. Note that synchronization to
		the end of the measurement is possible only in single sweep mode. For more information see 'Analyzing Several Traces -
		Trace Mode'. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Trace')
			:return: mode: WRITe Overwrite mode: the trace is overwritten by each sweep. This is the default setting. AVERage The average is formed over several sweeps. The 'Sweep/Average Count' determines the number of averaging procedures. MAXHold The maximum value is determined over several sweeps and displayed. The R&S FSW saves the sweep result in the trace memory only if the new value is greater than the previous one. MINHold The minimum value is determined from several measurements and displayed. The R&S FSW saves the sweep result in the trace memory only if the new value is lower than the previous one. VIEW The current contents of the trace memory are frozen and displayed. BLANk Hides the selected trace."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TRACe{trace_cmd_val}:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.TraceModeJ)
