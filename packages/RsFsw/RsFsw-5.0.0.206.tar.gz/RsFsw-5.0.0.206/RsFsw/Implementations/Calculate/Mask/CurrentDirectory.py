from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CurrentDirectory:
	"""CurrentDirectory commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("currentDirectory", core, parent)

	def set(self, subdirectory: str, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:MASK:CDIRectory \n
		Snippet: driver.calculate.mask.currentDirectory.set(subdirectory = '1', window = repcap.Window.Default) \n
		This command selects the directory the R&S FSW stores frequency masks in. \n
			:param subdirectory: String containing the path to the directory. The directory has to be a subdirectory of the default directory. Thus the path is always relative to the default directory (C:/R_S/INSTR/freqmask) . An empty string selects the default directory.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.value_to_quoted_str(subdirectory)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:MASK:CDIRectory {param}')

	def get(self, window=repcap.Window.Default) -> str:
		"""SCPI: CALCulate<n>:MASK:CDIRectory \n
		Snippet: value: str = driver.calculate.mask.currentDirectory.get(window = repcap.Window.Default) \n
		This command selects the directory the R&S FSW stores frequency masks in. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: subdirectory: String containing the path to the directory. The directory has to be a subdirectory of the default directory. Thus the path is always relative to the default directory (C:/R_S/INSTR/freqmask) . An empty string selects the default directory."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MASK:CDIRectory?')
		return trim_str_response(response)
