from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	@property
	def x(self):
		"""x commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_x'):
			from .X import X
			self._x = X(self._core, self._cmd_group)
		return self._x

	def get(self, trace_type: enums.TraceTypeList, window=repcap.Window.Default) -> List[float]:
		"""SCPI: TRACe<n>[:DATA] \n
		Snippet: value: List[float] = driver.applications.k91Wlan.trace.data.get(trace_type = enums.TraceTypeList.LIST, window = repcap.Window.Default) \n
		This command queries current trace data and measurement results from the window previously selected using method RsFsw.
		Applications.K10x_Lte.Display.Window.Subwindow.Select.set. As opposed to the R&S FSW base unit, the window suffix <n> is
		not considered in the R&S FSW WLAN application! Use the method RsFsw.Applications.K10x_Lte.Display.Window.Subwindow.
		Select.set to select the (sub) window before you query trace results! For details see 'Measurement results for
		TRACe<n>[:DATA]? TRACE<n>'. \n
			:param trace_type: TRACe1 | TRACe2 | TRACe3 | TRACe4 | TRACe5 | TRACe6 | LIST Selects the type of result to be returned. TRACE1 | ... | TRACE6 Returns the trace data for the corresponding trace. Note that for the default WLAN I/Q measurement (Modulation Accuracy, Flatness and Tolerance) , only 1 trace per window (TRACE1) is available. LIST Returns the results of the peak list evaluation for Spectrum Emission Mask measurements.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trace')
			:return: trace_ydata: No help available"""
		param = Conversions.enum_scalar_to_str(trace_type, enums.TraceTypeList)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_bin_or_ascii_float_list_with_opc(f'FORMAT REAL,32;TRACe{window_cmd_val}:DATA? {param}')
		return response

	def clone(self) -> 'Data':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Data(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
