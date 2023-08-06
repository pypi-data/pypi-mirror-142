from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Size:
	"""Size commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("size", core, parent)

	def set(self, state: enums.Size, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:SIZE \n
		Snippet: driver.applications.k9X11Ad.display.window.size.set(state = enums.Size.LARGe, window = repcap.Window.Default) \n
		This command maximizes the size of the selected result display window temporarily. To change the size of several windows
		on the screen permanently, use the method RsFsw.Applications.K17_Mcgd.Layout.Splitter.set command (see method RsFsw.
		Applications.K17_Mcgd.Layout.Splitter.set) . \n
			:param state: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.enum_scalar_to_str(state, enums.Size)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:SIZE {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.Size:
		"""SCPI: DISPlay[:WINDow<n>]:SIZE \n
		Snippet: value: enums.Size = driver.applications.k9X11Ad.display.window.size.get(window = repcap.Window.Default) \n
		This command maximizes the size of the selected result display window temporarily. To change the size of several windows
		on the screen permanently, use the method RsFsw.Applications.K17_Mcgd.Layout.Splitter.set command (see method RsFsw.
		Applications.K17_Mcgd.Layout.Splitter.set) . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: state: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:SIZE?')
		return Conversions.str_to_scalar_enum(response, enums.Size)
