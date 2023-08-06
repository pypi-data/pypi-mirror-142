from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Truncate:
	"""Truncate commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("truncate", core, parent)

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:PSPectrum:COLor:TRUNcate \n
		Snippet: driver.display.window.pspectrum.color.truncate.set(state = False, window = repcap.Window.Default) \n
		This command reduces the range of the color map of the persistence spectrum if there are no hits at the start or end of
		the value range. \n
			:param state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:PSPectrum:COLor:TRUNcate {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: DISPlay[:WINDow<n>]:PSPectrum:COLor:TRUNcate \n
		Snippet: value: bool = driver.display.window.pspectrum.color.truncate.get(window = repcap.Window.Default) \n
		This command reduces the range of the color map of the persistence spectrum if there are no hits at the start or end of
		the value range. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: state: ON | OFF | 0 | 1 OFF | 0 Switches the function off ON | 1 Switches the function on"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:PSPectrum:COLor:TRUNcate?')
		return Conversions.str_to_bool(response)
