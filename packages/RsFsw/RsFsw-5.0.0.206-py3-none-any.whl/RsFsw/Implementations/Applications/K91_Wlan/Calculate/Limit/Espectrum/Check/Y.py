from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Y:
	"""Y commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("y", core, parent)

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> float:
		"""SCPI: CALCulate<n>:LIMit<li>:ESPectrum:CHECk:Y \n
		Snippet: value: float = driver.applications.k91Wlan.calculate.limit.espectrum.check.y.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		Returns the highest (absolute) power level that exceeds the SEM limit. If no limit was exceeded, an error is returned. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: worst_value: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum:CHECk:Y?')
		return Conversions.str_to_float(response)
