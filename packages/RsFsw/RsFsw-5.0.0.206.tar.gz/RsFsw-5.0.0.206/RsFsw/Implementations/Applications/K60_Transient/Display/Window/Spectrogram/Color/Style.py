from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Style:
	"""Style commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("style", core, parent)

	def set(self, color_scheme: enums.ColorSchemeA, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:SPECtrogram:COLor[:STYLe] \n
		Snippet: driver.applications.k60Transient.display.window.spectrogram.color.style.set(color_scheme = enums.ColorSchemeA.COLD, window = repcap.Window.Default) \n
		This command selects the color scheme. For details see 'Color maps'. \n
			:param color_scheme: HOT Uses a color range from blue to red. Blue colors indicate low levels, red colors indicate high ones. COLD Uses a color range from red to blue. Red colors indicate low levels, blue colors indicate high ones. RADar Uses a color range from black over green to light turquoise with shades of green in between. GRAYscale Shows the results in shades of gray.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.enum_scalar_to_str(color_scheme, enums.ColorSchemeA)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:SPECtrogram:COLor:STYLe {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.ColorSchemeA:
		"""SCPI: DISPlay[:WINDow<n>]:SPECtrogram:COLor[:STYLe] \n
		Snippet: value: enums.ColorSchemeA = driver.applications.k60Transient.display.window.spectrogram.color.style.get(window = repcap.Window.Default) \n
		This command selects the color scheme. For details see 'Color maps'. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: color_scheme: HOT Uses a color range from blue to red. Blue colors indicate low levels, red colors indicate high ones. COLD Uses a color range from red to blue. Red colors indicate low levels, blue colors indicate high ones. RADar Uses a color range from black over green to light turquoise with shades of green in between. GRAYscale Shows the results in shades of gray."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:SPECtrogram:COLor:STYLe?')
		return Conversions.str_to_scalar_enum(response, enums.ColorSchemeA)
