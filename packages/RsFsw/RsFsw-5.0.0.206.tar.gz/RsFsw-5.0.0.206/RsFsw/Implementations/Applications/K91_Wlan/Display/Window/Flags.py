from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Flags:
	"""Flags commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("flags", core, parent)

	def set(self, state: float, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:FLAGs \n
		Snippet: driver.applications.k91Wlan.display.window.flags.set(state = 1.0, window = repcap.Window.Default) \n
		Configures the output of bitstream data in ASCII format \n
			:param state: 0 | 2 0 Switches the function off 2 In bitstream trace results, any DC (empty) carriers found in the bitstream are indicated by NULL in the bitstream, if the output format is ASCII.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.decimal_value_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:FLAGs {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: DISPlay[:WINDow<n>]:FLAGs \n
		Snippet: value: float = driver.applications.k91Wlan.display.window.flags.get(window = repcap.Window.Default) \n
		Configures the output of bitstream data in ASCII format \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: state: 0 | 2 0 Switches the function off 2 In bitstream trace results, any DC (empty) carriers found in the bitstream are indicated by NULL in the bitstream, if the output format is ASCII."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:FLAGs?')
		return Conversions.str_to_float(response)
