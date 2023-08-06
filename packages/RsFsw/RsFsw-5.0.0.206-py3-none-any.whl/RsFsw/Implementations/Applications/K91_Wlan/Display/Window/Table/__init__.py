from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Table:
	"""Table commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("table", core, parent)

	@property
	def item(self):
		"""item commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_item'):
			from .Item import Item
			self._item = Item(self._core, self._cmd_group)
		return self._item

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TABLe \n
		Snippet: driver.applications.k91Wlan.display.window.table.set(state = False, window = repcap.Window.Default) \n
		Displays or removes the Result Summary Global window. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Removes the Result Summary Global window ON | 1 Displays the Result Summary Global window
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TABLe {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: DISPlay[:WINDow<n>]:TABLe \n
		Snippet: value: bool = driver.applications.k91Wlan.display.window.table.get(window = repcap.Window.Default) \n
		Displays or removes the Result Summary Global window. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Removes the Result Summary Global window ON | 1 Displays the Result Summary Global window"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TABLe?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Table':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Table(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
