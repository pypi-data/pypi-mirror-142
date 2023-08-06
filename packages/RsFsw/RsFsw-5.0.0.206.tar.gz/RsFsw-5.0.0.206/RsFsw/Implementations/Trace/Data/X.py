from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class X:
	"""X commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("x", core, parent)

	def get(self, trace_type: enums.TraceNumber, window=repcap.Window.Default) -> List[float]:
		"""SCPI: TRACe<n>[:DATA]:X \n
		Snippet: value: List[float] = driver.trace.data.x.get(trace_type = enums.TraceNumber.BTOBits, window = repcap.Window.Default) \n
		This command queries the horizontal trace data for each sweep point in the specified window, for example the frequency in
		frequency domain or the time in time domain measurements. This is especially useful for traces with non-equidistant
		x-values. \n
			:param trace_type: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trace')
			:return: trace_xdata: No help available"""
		param = Conversions.enum_scalar_to_str(trace_type, enums.TraceNumber)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_bin_or_ascii_float_list_with_opc(f'FORMAT REAL,32;TRACe{window_cmd_val}:DATA:X? {param}')
		return response
