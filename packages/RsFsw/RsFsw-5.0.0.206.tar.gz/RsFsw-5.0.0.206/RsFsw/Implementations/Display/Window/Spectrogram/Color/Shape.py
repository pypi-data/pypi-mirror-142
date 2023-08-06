from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Shape:
	"""Shape commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("shape", core, parent)

	def set(self, shape: float, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:SPECtrogram:COLor:SHAPe \n
		Snippet: driver.display.window.spectrogram.color.shape.set(shape = 1.0, window = repcap.Window.Default) \n
		This command defines the shape and focus of the color curve for the spectrogram result display. \n
			:param shape: Shape of the color curve. Range: -1 to 1
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.decimal_value_to_str(shape)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:SPECtrogram:COLor:SHAPe {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: DISPlay[:WINDow<n>]:SPECtrogram:COLor:SHAPe \n
		Snippet: value: float = driver.display.window.spectrogram.color.shape.get(window = repcap.Window.Default) \n
		This command defines the shape and focus of the color curve for the spectrogram result display. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: shape: Shape of the color curve. Range: -1 to 1"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:SPECtrogram:COLor:SHAPe?')
		return Conversions.str_to_float(response)
