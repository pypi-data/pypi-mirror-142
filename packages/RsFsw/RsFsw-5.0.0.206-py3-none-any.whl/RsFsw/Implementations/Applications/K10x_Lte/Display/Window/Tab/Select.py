from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, window=repcap.Window.Default, tab=repcap.Tab.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TAB<tab>:SELect \n
		Snippet: driver.applications.k10Xlte.display.window.tab.select.set(window = repcap.Window.Default, tab = repcap.Tab.Default) \n
		This command selects a tab in diagrams with multiple subwindows (or views) . Note that selecting a tab does not actually
		select a subwindow. To select a subwindow, for example to query the results of a subwindow, use method RsFsw.Applications.
		K10x_Lte.Display.Window.Subwindow.Select.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param tab: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tab')
		"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		tab_cmd_val = self._cmd_group.get_repcap_cmd_value(tab, repcap.Tab)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TAB{tab_cmd_val}:SELect')

	def set_with_opc(self, window=repcap.Window.Default, tab=repcap.Tab.Default, opc_timeout_ms: int = -1) -> None:
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		tab_cmd_val = self._cmd_group.get_repcap_cmd_value(tab, repcap.Tab)
		"""SCPI: DISPlay[:WINDow<n>]:TAB<tab>:SELect \n
		Snippet: driver.applications.k10Xlte.display.window.tab.select.set_with_opc(window = repcap.Window.Default, tab = repcap.Tab.Default) \n
		This command selects a tab in diagrams with multiple subwindows (or views) . Note that selecting a tab does not actually
		select a subwindow. To select a subwindow, for example to query the results of a subwindow, use method RsFsw.Applications.
		K10x_Lte.Display.Window.Subwindow.Select.set. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param tab: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Tab')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'DISPlay:WINDow{window_cmd_val}:TAB{tab_cmd_val}:SELect', opc_timeout_ms)
