from typing import List

from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Data:
	"""Data commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("data", core, parent)

	def set(self, limit_line_points: List[float], window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:CONTrol[:DATA] \n
		Snippet: driver.applications.k40PhaseNoise.calculate.limit.control.data.set(limit_line_points = [1.1, 2.2, 3.3], window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command defines the horizontal definition points of a limit line. \n
			:param limit_line_points: Variable number of x-axis values. Note that the number of horizontal values has to be the same as the number of vertical values set with method RsFsw.Calculate.Limit.Lower.Data.set or method RsFsw.Calculate.Limit.Upper.Data.set. If not, the R&S FSW either adds missing values or ignores surplus values. The unit is Hz. Unit: HZ
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.list_to_csv_str(limit_line_points)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:CONTrol:DATA {param}')

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> List[float]:
		"""SCPI: CALCulate<n>:LIMit<li>:CONTrol[:DATA] \n
		Snippet: value: List[float] = driver.applications.k40PhaseNoise.calculate.limit.control.data.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command defines the horizontal definition points of a limit line. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: limit_line_points: Variable number of x-axis values. Note that the number of horizontal values has to be the same as the number of vertical values set with method RsFsw.Calculate.Limit.Lower.Data.set or method RsFsw.Calculate.Limit.Upper.Data.set. If not, the R&S FSW either adds missing values or ignores surplus values. The unit is Hz. Unit: HZ"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_bin_or_ascii_float_list(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:CONTrol:DATA?')
		return response
