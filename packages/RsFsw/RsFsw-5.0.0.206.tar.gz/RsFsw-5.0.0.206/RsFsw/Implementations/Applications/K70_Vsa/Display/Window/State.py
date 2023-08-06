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
		"""SCPI: DISPlay[:WINDow<n>]:STATe \n
		Snippet: driver.applications.k70Vsa.display.window.state.set(state = False, window = repcap.Window.Default) \n
		Activates or deactivates the specified window. Note that this command is maintained for compatibility reasons only. Use
		the LAYout commands for new remote control programs (see 'Working with windows in the display') . \n
			:param state: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:STATe {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: DISPlay[:WINDow<n>]:STATe \n
		Snippet: value: bool = driver.applications.k70Vsa.display.window.state.get(window = repcap.Window.Default) \n
		Activates or deactivates the specified window. Note that this command is maintained for compatibility reasons only. Use
		the LAYout commands for new remote control programs (see 'Working with windows in the display') . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: state: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:STATe?')
		return Conversions.str_to_bool(response)
