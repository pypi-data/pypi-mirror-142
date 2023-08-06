from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ldelta:
	"""Ldelta commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ldelta", core, parent)

	def get(self, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default, limitIx=repcap.LimitIx.Default) -> float:
		"""SCPI: CALCulate<n>:DELTamarker<m>:FUNCtion:FMEasurement:LIMit<li>:LDELta \n
		Snippet: value: float = driver.calculate.deltaMarker.function.fmeasurement.limit.ldelta.get(window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default, limitIx = repcap.LimitIx.Default) \n
		This command queries the vertical distance from the marker position to the limit line. The unit is dB. If the marker has
		been assigned to a different trace than the limit line, or if no limit ine is defined for the marker position, the
		command returns -200. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: amplitude: Vertical distance to the limit line in dB."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:FUNCtion:FMEasurement:LIMit{limitIx_cmd_val}:LDELta?')
		return Conversions.str_to_float(response)
