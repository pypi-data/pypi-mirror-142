from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.MarkerMode, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:BPOWer:MODE \n
		Snippet: driver.calculate.marker.function.bpower.mode.set(mode = enums.MarkerMode.DENSity, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command selects the way the results for a band power marker are displayed. (Note: relative power results are only
		availabe for delta markers, see .method RsFsw.Calculate.DeltaMarker.Function.Bpower.Mode.set \n
			:param mode: POWer Result is displayed as an absolute power. The power unit depends on the method RsFsw.Applications.K91_Wlan.Calculate.Unit.Power.set setting. DENSity Result is displayed as a density in dBm/Hz.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.MarkerMode)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:BPOWer:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> enums.MarkerMode:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:BPOWer:MODE \n
		Snippet: value: enums.MarkerMode = driver.calculate.marker.function.bpower.mode.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command selects the way the results for a band power marker are displayed. (Note: relative power results are only
		availabe for delta markers, see .method RsFsw.Calculate.DeltaMarker.Function.Bpower.Mode.set \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: mode: POWer Result is displayed as an absolute power. The power unit depends on the method RsFsw.Applications.K91_Wlan.Calculate.Unit.Power.set setting. DENSity Result is displayed as a density in dBm/Hz."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:BPOWer:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.MarkerMode)
