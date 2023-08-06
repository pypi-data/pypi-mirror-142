from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Full:
	"""Full commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("full", core, parent)

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> List[float]:
		"""SCPI: CALCulate<n>:LIMit<li>:LOWer:FULL \n
		Snippet: value: List[float] = driver.applications.k91Wlan.calculate.limit.lower.full.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command queries the limit line y-values as defined by the standard for the specified window. Tip: to query the
		corresponding x-values, use the method RsFsw.Trace.Data.X.get_ command. Note: both commands have the same effect; the
		suffix determines whether the upper or lower limit is returned. For compatibility reasons, both commands are maintained. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: limit_values: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_bin_or_ascii_float_list(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:LOWer:FULL?')
		return response
