from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lcondition:
	"""Lcondition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lcondition", core, parent)

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default, limitIx=repcap.LimitIx.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:FMEasurement:LIMit<li>:LCONdition \n
		Snippet: value: float = driver.calculate.marker.function.fmeasurement.limit.lcondition.get(window = repcap.Window.Default, marker = repcap.Marker.Default, limitIx = repcap.LimitIx.Default) \n
		This command queries the condition of a marker position in relation to a certain limit line. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: condition: 0 The marker has passed the limit check. 1 The marker is inside the margins of a limit line. 2 The marker has failed the limit check."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:FMEasurement:LIMit{limitIx_cmd_val}:LCONdition?')
		return Conversions.str_to_float(response)
