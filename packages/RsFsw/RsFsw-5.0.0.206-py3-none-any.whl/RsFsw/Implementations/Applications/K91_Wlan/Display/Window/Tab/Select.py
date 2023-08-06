from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, subwindow_name: str = None, window=repcap.Window.Default, tab=repcap.Tab.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TAB<1..n>:SELect \n
		Snippet: driver.applications.k91Wlan.display.window.tab.select.set(subwindow_name = '1', window = repcap.Window.Default, tab = repcap.Tab.Default) \n
		This command sets the focus on the selected result display subwindow for measurements with multiple result windows (MIMO)
		. The subwindow is selected either by its number (<No> suffix) or by its name (<SubWindowName> parameter) . This window
		is then the active window. Use this command to select the (sub) window before querying trace data. \n
			:param subwindow_name: Name of the subwindow
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param tab: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tab')
		"""
		param = ''
		if subwindow_name:
			param = Conversions.value_to_quoted_str(subwindow_name)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		tab_cmd_val = self._cmd_group.get_repcap_cmd_value(tab, repcap.Tab)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TAB{tab_cmd_val}:SELect {param}'.strip())
