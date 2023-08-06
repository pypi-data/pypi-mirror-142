from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trend:
	"""Trend commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trend", core, parent)

	def set(self, state: bool, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default) -> None:
		"""SCPI: CALCulate<n>:DELTamarker<m>:LINK:TRENd \n
		Snippet: driver.applications.k6Pulse.calculate.deltaMarker.link.trend.set(state = False, window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		If enabled, marker M1 in Parameter Trend displays is linked to the pulse selection. Thus, if you move the marker M1 to a
		different pulse, the 'Pulse selection' is set to the same pulse, and vice versa. This command requires the markers to be
		linked across all windows (method RsFsw.Applications.K9x_11ad.Calculate.Marker.Link.set ON) . If the method RsFsw.
		Applications.K6_Pulse.Calculate.Marker.Link.Trend.set command is enabled, the method RsFsw.Applications.K9x_11ad.
		Calculate.Marker.Link.set command is automatically also enabled, if necessary. \n
			:param state: ON | OFF | 1 | 0
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		self._core.io.write_with_opc(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:LINK:TRENd {param}')

	def get(self, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default) -> bool:
		"""SCPI: CALCulate<n>:DELTamarker<m>:LINK:TRENd \n
		Snippet: value: bool = driver.applications.k6Pulse.calculate.deltaMarker.link.trend.get(window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		If enabled, marker M1 in Parameter Trend displays is linked to the pulse selection. Thus, if you move the marker M1 to a
		different pulse, the 'Pulse selection' is set to the same pulse, and vice versa. This command requires the markers to be
		linked across all windows (method RsFsw.Applications.K9x_11ad.Calculate.Marker.Link.set ON) . If the method RsFsw.
		Applications.K6_Pulse.Calculate.Marker.Link.Trend.set command is enabled, the method RsFsw.Applications.K9x_11ad.
		Calculate.Marker.Link.set command is automatically also enabled, if necessary. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
			:return: state: ON | OFF | 1 | 0"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		response = self._core.io.query_str_with_opc(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:LINK:TRENd?')
		return Conversions.str_to_bool(response)
