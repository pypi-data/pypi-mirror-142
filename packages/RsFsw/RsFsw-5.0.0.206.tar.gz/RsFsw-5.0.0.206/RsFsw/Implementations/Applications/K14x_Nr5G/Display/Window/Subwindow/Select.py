from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:SELect \n
		Snippet: driver.applications.k14Xnr5G.display.window.subwindow.select.set(window = repcap.Window.Default, subWindow = repcap.SubWindow.Default) \n
		This command sets the focus on the selected result display window. This window is then the active window.
		For measurements with multiple results in subwindows, the command also selects the subwindow. Use this command to select
		the (sub) window before querying trace data. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
		"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:SELect')

	def set_with_opc(self, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default, opc_timeout_ms: int = -1) -> None:
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:SELect \n
		Snippet: driver.applications.k14Xnr5G.display.window.subwindow.select.set_with_opc(window = repcap.Window.Default, subWindow = repcap.SubWindow.Default) \n
		This command sets the focus on the selected result display window. This window is then the active window.
		For measurements with multiple results in subwindows, the command also selects the subwindow. Use this command to select
		the (sub) window before querying trace data. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:SELect', opc_timeout_ms)
