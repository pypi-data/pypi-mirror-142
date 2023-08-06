from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mtable:
	"""Mtable commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mtable", core, parent)

	def set(self, state: enums.AutoMode, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:MTABle \n
		Snippet: driver.applications.k9X11Ad.display.window.mtable.set(state = enums.AutoMode.AUTO, window = repcap.Window.Default) \n
		This command turns the marker table on and off. \n
			:param state: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.enum_scalar_to_str(state, enums.AutoMode)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:MTABle {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.AutoMode:
		"""SCPI: DISPlay[:WINDow<n>]:MTABle \n
		Snippet: value: enums.AutoMode = driver.applications.k9X11Ad.display.window.mtable.get(window = repcap.Window.Default) \n
		This command turns the marker table on and off. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: state: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:MTABle?')
		return Conversions.str_to_scalar_enum(response, enums.AutoMode)
