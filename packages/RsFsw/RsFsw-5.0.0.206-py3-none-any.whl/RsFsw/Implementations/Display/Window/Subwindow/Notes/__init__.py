from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Notes:
	"""Notes commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("notes", core, parent)

	@property
	def text(self):
		"""text commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_text'):
			from .Text import Text
			self._text = Text(self._core, self._cmd_group)
		return self._text

	@property
	def append(self):
		"""append commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_append'):
			from .Append import Append
			self._append = Append(self._core, self._cmd_group)
		return self._append

	def clear(self, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:NOTes:CLEar \n
		Snippet: driver.display.window.subwindow.notes.clear(window = repcap.Window.Default, subWindow = repcap.SubWindow.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
		"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:NOTes:CLEar')

	def clear_with_opc(self, window=repcap.Window.Default, subWindow=repcap.SubWindow.Default, opc_timeout_ms: int = -1) -> None:
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		subWindow_cmd_val = self._cmd_group.get_repcap_cmd_value(subWindow, repcap.SubWindow)
		"""SCPI: DISPlay[:WINDow<n>][:SUBWindow<w>]:NOTes:CLEar \n
		Snippet: driver.display.window.subwindow.notes.clear_with_opc(window = repcap.Window.Default, subWindow = repcap.SubWindow.Default) \n
		No command help available \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:param subWindow: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Subwindow')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'DISPlay:WINDow{window_cmd_val}:SUBWindow{subWindow_cmd_val}:NOTes:CLEar', opc_timeout_ms)

	def clone(self) -> 'Notes':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Notes(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
