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

	def set(self, trace: List[float], window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:PNLimit:TRACe \n
		Snippet: driver.applications.k40PhaseNoise.calculate.pnLimit.trace.set(trace = [1.1, 2.2, 3.3], window = repcap.Window.Default) \n
		This command selects the trace to assign a phase noise limit line to. \n
			:param trace: Range: 1 to 6
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.list_to_csv_str(trace)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:PNLimit:TRACe {param}')

	def get(self, window=repcap.Window.Default) -> List[float]:
		"""SCPI: CALCulate<n>:PNLimit:TRACe \n
		Snippet: value: List[float] = driver.applications.k40PhaseNoise.calculate.pnLimit.trace.get(window = repcap.Window.Default) \n
		This command selects the trace to assign a phase noise limit line to. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: trace: Range: 1 to 6"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_bin_or_ascii_float_list(f'CALCulate{window_cmd_val}:PNLimit:TRACe?')
		return response
