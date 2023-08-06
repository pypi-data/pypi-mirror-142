from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Coupling:
	"""Coupling commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("coupling", core, parent)

	def set(self, state: bool, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:COUPling \n
		Snippet: driver.applications.k14Xnr5G.display.window.subwindow.coupling.set(state = False, window = repcap.Window.Default, subWindow = repcap.SubWindow.Default) \n
		This command couples or decouples result display tabs (subwindows) . Subwindow coupling is available for measurements
		with multiple data streams (like carrier aggregation) . \n
			:param state: ON | OFF | 1 | 0
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:COUPling {param}')

	def get(self, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default) -> bool:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:COUPling \n
		Snippet: value: bool = driver.applications.k14Xnr5G.display.window.subwindow.coupling.get(window = repcap.Window.Default, subWindow = repcap.SubWindow.Default) \n
		This command couples or decouples result display tabs (subwindows) . Subwindow coupling is available for measurements
		with multiple data streams (like carrier aggregation) . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:return: state: ON | OFF | 1 | 0"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:COUPling?')
		return Conversions.str_to_bool(response)
