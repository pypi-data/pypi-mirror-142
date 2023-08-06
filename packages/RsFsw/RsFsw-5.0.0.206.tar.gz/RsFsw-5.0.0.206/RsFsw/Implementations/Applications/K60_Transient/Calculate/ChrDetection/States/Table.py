from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Table:
	"""Table commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("table", core, parent)

	def load(self, filename: str, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:CHRDetection:STATes:TABLe:LOAD \n
		Snippet: driver.applications.k60Transient.calculate.chrDetection.states.table.load(filename = '1', window = repcap.Window.Default) \n
		Loads the signal state table configuration from the selected file. \n
			:param filename: String containing the path and name of the file.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.value_to_quoted_str(filename)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:CHRDetection:STATes:TABLe:LOAD {param}')

	def save(self, filename: str, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:CHRDetection:STATes:TABLe:SAVE \n
		Snippet: driver.applications.k60Transient.calculate.chrDetection.states.table.save(filename = '1', window = repcap.Window.Default) \n
		Saves the current signal state table configuration to a file for later use. \n
			:param filename: String containing the path and name of the file.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.value_to_quoted_str(filename)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:CHRDetection:STATes:TABLe:SAVE {param}')
