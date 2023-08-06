from typing import List

from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trace:
	"""Trace commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trace", core, parent)

	def set(self, trace_limit: List[float], window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:TRACe \n
		Snippet: driver.applications.k30NoiseFigure.calculate.limit.trace.set(trace_limit = [1.1, 2.2, 3.3], window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command links a limit line to one or more traces. Note that this command is maintained for compatibility reasons
		only. Limit lines no longer need to be assigned to a trace explicitly. The trace to be checked can be defined directly
		(as a suffix) in the new command to activate the limit check (see method RsFsw.Calculate.Limit.Trace.Check.set) . \n
			:param trace_limit: 1 to 4
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.list_to_csv_str(trace_limit)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:TRACe {param}')

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> List[float]:
		"""SCPI: CALCulate<n>:LIMit<li>:TRACe \n
		Snippet: value: List[float] = driver.applications.k30NoiseFigure.calculate.limit.trace.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command links a limit line to one or more traces. Note that this command is maintained for compatibility reasons
		only. Limit lines no longer need to be assigned to a trace explicitly. The trace to be checked can be defined directly
		(as a suffix) in the new command to activate the limit check (see method RsFsw.Calculate.Limit.Trace.Check.set) . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: trace_limit: 1 to 4"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_bin_or_ascii_float_list(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:TRACe?')
		return response
