from typing import List

from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Memory:
	"""Memory commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("memory", core, parent)

	def get(self, trace_type: enums.TraceNumber, points_offset: int, points_count: int, window=repcap.Window.Default) -> List[float]:
		"""SCPI: TRACe<n>[:DATA]:MEMory \n
		Snippet: value: List[float] = driver.trace.data.memory.get(trace_type = enums.TraceNumber.BTOBits, points_offset = 1, points_count = 1, window = repcap.Window.Default) \n
		This command queries the previously captured trace data for the specified trace from the memory. As an offset and number
		of sweep points to be retrieved can be specified, the trace data can be retrieved in smaller portions, making the command
		faster than the TRAC:DATA? command. This is useful if only specific parts of the trace data are of interest.
		If no parameters are specified with the command, the entire trace data is retrieved; in this case, the command returns
		the same results as TRAC:DATA? TRACE1. For details on the returned values see the TRAC:DATA? <TRACE...> command. \n
			:param trace_type: No help available
			:param points_offset: No help available
			:param points_count: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trace')
			:return: trace_ydata: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('trace_type', trace_type, DataType.Enum, enums.TraceNumber), ArgSingle('points_offset', points_offset, DataType.Integer), ArgSingle('points_count', points_count, DataType.Integer))
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_bin_or_ascii_float_list_with_opc(f'FORMAT REAL,32;TRACe{window_cmd_val}:DATA:MEMory? {param}'.rstrip())
		return response
