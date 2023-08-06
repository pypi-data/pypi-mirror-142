from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPy:
	"""FormatPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	def set(self, format_py: enums.TimeFormat, window=repcap.Window.Default) -> None:
		"""SCPI: DISPlay[:WINDow<n>]:TIME:FORMat \n
		Snippet: driver.display.window.time.formatPy.set(format_py = enums.TimeFormat.DE, window = repcap.Window.Default) \n
		This command selects the time and date format. \n
			:param format_py: US | DE DE dd.mm.yyyy hh:mm:ss 24 hour format. US mm/dd/yyyy hh:mm:ss 12 hour format.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.enum_scalar_to_str(format_py, enums.TimeFormat)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'DISPlay:WINDow{window_cmd_val}:TIME:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.TimeFormat:
		"""SCPI: DISPlay[:WINDow<n>]:TIME:FORMat \n
		Snippet: value: enums.TimeFormat = driver.display.window.time.formatPy.get(window = repcap.Window.Default) \n
		This command selects the time and date format. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: format_py: US | DE DE dd.mm.yyyy hh:mm:ss 24 hour format. US mm/dd/yyyy hh:mm:ss 12 hour format."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'DISPlay:WINDow{window_cmd_val}:TIME:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.TimeFormat)
