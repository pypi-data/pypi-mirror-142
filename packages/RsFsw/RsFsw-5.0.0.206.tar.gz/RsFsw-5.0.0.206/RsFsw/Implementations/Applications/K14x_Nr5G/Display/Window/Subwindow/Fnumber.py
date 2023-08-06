from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fnumber:
	"""Fnumber commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fnumber", core, parent)

	def set(self, frame: float, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:FNUMber \n
		Snippet: driver.applications.k14Xnr5G.display.window.subwindow.fnumber.set(frame = 1.0, window = repcap.Window.Default, subWindow = repcap.SubWindow.Default) \n
		This command assigns a specific frame to a view.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Capture more than one frame. \n
			:param frame: numeric value (integer only)
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
		"""
		param = Conversions.decimal_value_to_str(frame)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:FNUMber {param}')

	def get(self, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default) -> float:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:FNUMber \n
		Snippet: value: float = driver.applications.k14Xnr5G.display.window.subwindow.fnumber.get(window = repcap.Window.Default, subWindow = repcap.SubWindow.Default) \n
		This command assigns a specific frame to a view.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Capture more than one frame. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:return: frame: numeric value (integer only)"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:FNUMber?')
		return Conversions.str_to_float(response)
