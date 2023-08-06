from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, frames: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:SPECtrogram:FRAMe:COUNt \n
		Snippet: driver.calculate.spectrogram.frame.count.set(frames = 1.0, window = repcap.Window.Default) \n
		This command defines the number of frames to be recorded in a single sweep. This value applies to all spectrograms in the
		channel. \n
			:param frames: The maximum number of frames depends on the history depth. Range: 1 to history depth
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(frames)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:SPECtrogram:FRAMe:COUNt {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:SPECtrogram:FRAMe:COUNt \n
		Snippet: value: float = driver.calculate.spectrogram.frame.count.get(window = repcap.Window.Default) \n
		This command defines the number of frames to be recorded in a single sweep. This value applies to all spectrograms in the
		channel. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: frames: The maximum number of frames depends on the history depth. Range: 1 to history depth"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:SPECtrogram:FRAMe:COUNt?')
		return Conversions.str_to_float(response)
