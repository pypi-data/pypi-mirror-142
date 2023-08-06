from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frame:
	"""Frame commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frame", core, parent)

	def set(self, frame: float, window=repcap.Window.Default, marker=repcap.Marker.Default) -> None:
		"""SCPI: CALCulate<n>:MARKer<m>:SPECtrogram:FRAMe \n
		Snippet: driver.calculate.marker.spectrogram.frame.set(frame = 1.0, window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command positions a marker on a particular frame. \n
			:param frame: Selects a frame directly by the frame number. Valid if the time stamp is off. The range depends on the history depth. Unit: S
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
		"""
		param = Conversions.decimal_value_to_str(frame)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		self._core.io.write(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:SPECtrogram:FRAMe {param}')

	def get(self, window=repcap.Window.Default, marker=repcap.Marker.Default) -> float:
		"""SCPI: CALCulate<n>:MARKer<m>:SPECtrogram:FRAMe \n
		Snippet: value: float = driver.calculate.marker.spectrogram.frame.get(window = repcap.Window.Default, marker = repcap.Marker.Default) \n
		This command positions a marker on a particular frame. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param marker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Marker')
			:return: frame: Selects a frame directly by the frame number. Valid if the time stamp is off. The range depends on the history depth. Unit: S"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		marker_cmd_val = self._cmd_group.get_repcap_cmd_value(marker, repcap.Marker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MARKer{marker_cmd_val}:SPECtrogram:FRAMe?')
		return Conversions.str_to_float(response)
