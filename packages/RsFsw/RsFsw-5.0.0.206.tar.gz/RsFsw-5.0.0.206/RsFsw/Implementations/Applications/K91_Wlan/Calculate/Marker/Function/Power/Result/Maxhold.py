from typing import List

from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maxhold:
	"""Maxhold commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maxhold", core, parent)

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> List[float]:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:POWer:RESult:MAXHold \n
		Snippet: value: List[float] = driver.applications.k91Wlan.calculate.marker.function.power.result.maxhold.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		Returns a comma-separated list of the maxhold trace results for power measurements. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: trace_results: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_bin_or_ascii_float_list_with_opc(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:POWer:RESult:MAXHold?')
		return response
