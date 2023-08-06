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

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:MINFo[:STATe] \n
		Snippet: driver.applications.k18AmplifierEt.display.window.minfo.state.set(state = False, window = repcap.Window.Default) \n
		This command turns the marker information in all diagrams on and off. \n
			:param state: ON | 1 Displays the marker information in the diagrams. OFF | 0 Hides the marker information in the diagrams.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:MINFo:STATe {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: DISPlay[:WINDow<n>]:MINFo[:STATe] \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.display.window.minfo.state.get(window = repcap.Window.Default) \n
		This command turns the marker information in all diagrams on and off. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: state: ON | 1 Displays the marker information in the diagrams. OFF | 0 Hides the marker information in the diagrams."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:MINFo:STATe?')
		return Conversions.str_to_bool(response)
