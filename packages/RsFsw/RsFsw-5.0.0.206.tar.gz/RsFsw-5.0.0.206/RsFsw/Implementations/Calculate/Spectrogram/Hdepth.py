from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hdepth:
	"""Hdepth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hdepth", core, parent)

	def set(self, history: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:SPECtrogram:HDEPth \n
		Snippet: driver.calculate.spectrogram.hdepth.set(history = 1.0, window = repcap.Window.Default) \n
		This command defines the number of frames to be stored in the R&S FSW memory. \n
			:param history: The maximum number of frames depends on the number of sweep points. Range: 781 to 20000
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(history)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:SPECtrogram:HDEPth {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:SPECtrogram:HDEPth \n
		Snippet: value: float = driver.calculate.spectrogram.hdepth.get(window = repcap.Window.Default) \n
		This command defines the number of frames to be stored in the R&S FSW memory. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: history: The maximum number of frames depends on the number of sweep points. Range: 781 to 20000"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:SPECtrogram:HDEPth?')
		return Conversions.str_to_float(response)
