from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, arg_0: bool, window=repcap.Window.Default) -> None:
		"""SCPI: HCOPy:ITEM:WINDow<1|2>:TABLe:STATe \n
		Snippet: driver.hardCopy.item.window.table.state.set(arg_0 = False, window = repcap.Window.Default) \n
		No command help available \n
			:param arg_0: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.bool_to_str(arg_0)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'HCOPy:ITEM:WINDow{window_cmd_val}:TABLe:STATe {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: HCOPy:ITEM:WINDow<1|2>:TABLe:STATe \n
		Snippet: value: bool = driver.hardCopy.item.window.table.state.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: arg_0: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'HCOPy:ITEM:WINDow{window_cmd_val}:TABLe:STATe?')
		return Conversions.str_to_bool(response)
