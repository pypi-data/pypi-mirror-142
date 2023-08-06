from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default, zoomWindow=repcap.ZoomWindow.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:ZOOM:MULTiple<zn>[:STATe] \n
		Snippet: driver.display.window.subwindow.zoom.multiple.state.set(state = False, window = repcap.Window.Default, subWindow = repcap.SubWindow.Default, zoomWindow = repcap.ZoomWindow.Default) \n
		This command turns the multiple zoom on and off. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:param zoomWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Multiple')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		zoomWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(zoomWindow, repcap.ZoomWindow)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:ZOOM:MULTiple{zoomWindow_cmd_val}:STATe {param}')

	def get(self, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default, zoomWindow=repcap.ZoomWindow.Default) -> bool:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:ZOOM:MULTiple<zn>[:STATe] \n
		Snippet: value: bool = driver.display.window.subwindow.zoom.multiple.state.get(window = repcap.Window.Default, subWindow = repcap.SubWindow.Default, zoomWindow = repcap.ZoomWindow.Default) \n
		This command turns the multiple zoom on and off. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:param zoomWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Multiple')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		zoomWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(zoomWindow, repcap.ZoomWindow)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:ZOOM:MULTiple{zoomWindow_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
