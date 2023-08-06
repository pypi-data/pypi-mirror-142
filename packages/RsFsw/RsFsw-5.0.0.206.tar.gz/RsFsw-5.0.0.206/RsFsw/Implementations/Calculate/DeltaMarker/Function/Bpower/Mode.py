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

	def set(self, mode: enums.MarkerMode, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default) -> None:
		"""SCPI: CALCulate<n>:DELTamarker<m>:FUNCtion:BPOWer:MODE \n
		Snippet: driver.calculate.deltaMarker.function.bpower.mode.set(mode = enums.MarkerMode.DENSity, window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		This command selects the way the results for a band power delta marker are displayed. \n
			:param mode: POWer Result is displayed as an absolute power. The power unit depends on the method RsFsw.Applications.K91_Wlan.Calculate.Unit.Power.set setting. DENSity Result is displayed as a density in dBm/Hz. RPOWer This setting is only available for a delta band power marker. The result is the difference between the absolute power in the band around the delta marker and the absolute power for the reference marker. The powers are subtracted logarithmically, so the result is a dB value. [Relative band power (Delta2) in dB] = [absolute band power (Delta2) in dBm] - [absolute (band) power of reference marker in dBm] For details see 'Relative band power markers'.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.MarkerMode)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		self._core.io.write(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:FUNCtion:BPOWer:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default) -> enums.MarkerMode:
		"""SCPI: CALCulate<n>:DELTamarker<m>:FUNCtion:BPOWer:MODE \n
		Snippet: value: enums.MarkerMode = driver.calculate.deltaMarker.function.bpower.mode.get(window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		This command selects the way the results for a band power delta marker are displayed. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
			:return: mode: POWer Result is displayed as an absolute power. The power unit depends on the method RsFsw.Applications.K91_Wlan.Calculate.Unit.Power.set setting. DENSity Result is displayed as a density in dBm/Hz. RPOWer This setting is only available for a delta band power marker. The result is the difference between the absolute power in the band around the delta marker and the absolute power for the reference marker. The powers are subtracted logarithmically, so the result is a dB value. [Relative band power (Delta2) in dB] = [absolute band power (Delta2) in dBm] - [absolute (band) power of reference marker in dBm] For details see 'Relative band power markers'."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:FUNCtion:BPOWer:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.MarkerMode)
