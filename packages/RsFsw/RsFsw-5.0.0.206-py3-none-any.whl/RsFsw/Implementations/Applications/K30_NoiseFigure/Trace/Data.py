from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def get(self, trace_type: enums.TraceTypeK30, window=repcap.Window.Default) -> List[float]:
		"""SCPI: TRACe<n>[:DATA] \n
		Snippet: value: List[float] = driver.applications.k30NoiseFigure.trace.data.get(trace_type = enums.TraceTypeK30.TRACe1, window = repcap.Window.Default) \n
		This command queries the noise figure measurement results. \n
			:param trace_type: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Trace')
			:return: trace_data: For any graphical result display, the command returns one result for each measurement point. The unit depends on the result you are querying."""
		param = Conversions.enum_scalar_to_str(trace_type, enums.TraceTypeK30)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_bin_or_ascii_float_list_with_opc(f'FORMAT REAL,32;TRACe{window_cmd_val}:DATA? {param}')
		return response
