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

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: HCOPy:ITEM:WINDow<1|2>:TRACe:STATe \n
		Snippet: driver.hardCopy.item.window.trace.state.set(state = False, window = repcap.Window.Default) \n
		No command help available \n
			:param state: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'HCOPy:ITEM:WINDow{window_cmd_val}:TRACe:STATe {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: HCOPy:ITEM:WINDow<1|2>:TRACe:STATe \n
		Snippet: value: bool = driver.hardCopy.item.window.trace.state.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: state: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'HCOPy:ITEM:WINDow{window_cmd_val}:TRACe:STATe?')
		return Conversions.str_to_bool(response)
