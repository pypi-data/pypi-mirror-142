from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Threshold:
	"""Threshold commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("threshold", core, parent)

	def set(self, level: float, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:STRack:THReshold \n
		Snippet: driver.calculate.marker.function.strack.threshold.set(level = 1.0, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command defines the threshold level for the signal tracking process. Note that you have to turn on signal tracking
		before you can use the command. \n
			:param level: The unit depends on method RsFsw.Applications.K91_Wlan.Calculate.Unit.Power.set. Range: -130 dBm to 30 dBm, Unit: DBM
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.decimal_value_to_str(level)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:STRack:THReshold {param}')

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:FUNCtion:STRack:THReshold \n
		Snippet: value: float = driver.calculate.marker.function.strack.threshold.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command defines the threshold level for the signal tracking process. Note that you have to turn on signal tracking
		before you can use the command. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: level: The unit depends on method RsFsw.Applications.K91_Wlan.Calculate.Unit.Power.set. Range: -130 dBm to 30 dBm, Unit: DBM"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:FUNCtion:STRack:THReshold?')
		return Conversions.str_to_float(response)
