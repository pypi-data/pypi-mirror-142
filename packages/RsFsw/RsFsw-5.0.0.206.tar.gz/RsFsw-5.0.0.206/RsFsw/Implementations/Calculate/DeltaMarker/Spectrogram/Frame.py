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

	def set(self, frame: float, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default) -> None:
		"""SCPI: CALCulate<n>:DELTamarker<m>:SPECtrogram:FRAMe \n
		Snippet: driver.calculate.deltaMarker.spectrogram.frame.set(frame = 1.0, window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		This command positions a delta marker on a particular frame. The frame is relative to the position of marker 1.
		The command is available for the spectrogram. \n
			:param frame: Selects a frame either by its frame number or time stamp. The frame number is available if the time stamp is off. The range depends on the history depth. The time stamp is available if the time stamp is on. The number is the distance to frame 0 in seconds. The range depends on the history depth. Unit: S
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
		"""
		param = Conversions.decimal_value_to_str(frame)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		self._core.io.write(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:SPECtrogram:FRAMe {param}')

	def get(self, window=repcap.Window.Default, deltaMarker=repcap.DeltaMarker.Default) -> float:
		"""SCPI: CALCulate<n>:DELTamarker<m>:SPECtrogram:FRAMe \n
		Snippet: value: float = driver.calculate.deltaMarker.spectrogram.frame.get(window = repcap.Window.Default, deltaMarker = repcap.DeltaMarker.Default) \n
		This command positions a delta marker on a particular frame. The frame is relative to the position of marker 1.
		The command is available for the spectrogram. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param deltaMarker: optional repeated capability selector. Default value: Nr1 (settable in the interface 'DeltaMarker')
			:return: frame: Selects a frame either by its frame number or time stamp. The frame number is available if the time stamp is off. The range depends on the history depth. The time stamp is available if the time stamp is on. The number is the distance to frame 0 in seconds. The range depends on the history depth. Unit: S"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		deltaMarker_cmd_val = self._cmd_group.get_repcap_cmd_value(deltaMarker, repcap.DeltaMarker)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:DELTamarker{deltaMarker_cmd_val}:SPECtrogram:FRAMe?')
		return Conversions.str_to_float(response)
