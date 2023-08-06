from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def set(self, window_name: enums.WindowName, outputConnector=repcap.OutputConnector.Default) -> None:
		"""SCPI: OUTPut<up>:ADEMod[:ONLine]:SOURce \n
		Snippet: driver.output.ademod.online.source.set(window_name = enums.WindowName.FOCus, outputConnector = repcap.OutputConnector.Default) \n
		This command selects the result display whose results are output. Only active time domain results can be selected. \n
			:param window_name: (enum or string) string String containing the name of the window. By default, the name of a window is the same as its index. To determine the name and index of all active windows, use the method RsFsw.Layout.Catalog.Window.get_ query. FOCus Dynamically switches to the currently selected window. If a window is selected that does not contain a time-domain result display, the selection is ignored and the previous setting is maintained.
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.enum_ext_scalar_to_str(window_name, enums.WindowName)
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		self._core.io.write(f'OUTPut{outputConnector_cmd_val}:ADEMod:ONLine:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self, outputConnector=repcap.OutputConnector.Default) -> enums.WindowName:
		"""SCPI: OUTPut<up>:ADEMod[:ONLine]:SOURce \n
		Snippet: value: enums.WindowName = driver.output.ademod.online.source.get(outputConnector = repcap.OutputConnector.Default) \n
		This command selects the result display whose results are output. Only active time domain results can be selected. \n
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: window_name: (enum or string) string String containing the name of the window. By default, the name of a window is the same as its index. To determine the name and index of all active windows, use the method RsFsw.Layout.Catalog.Window.get_ query. FOCus Dynamically switches to the currently selected window. If a window is selected that does not contain a time-domain result display, the selection is ignored and the previous setting is maintained."""
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		response = self._core.io.query_str(f'OUTPut{outputConnector_cmd_val}:ADEMod:ONLine:SOURce?')
		return Conversions.str_to_scalar_enum_ext(response, enums.WindowName)
