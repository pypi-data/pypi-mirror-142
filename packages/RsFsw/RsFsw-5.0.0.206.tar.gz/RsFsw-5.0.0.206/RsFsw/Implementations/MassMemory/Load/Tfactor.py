from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tfactor:
	"""Tfactor commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tfactor", core, parent)

	def set(self, filename: str, window=repcap.Window.Default) -> None:
		"""SCPI: MMEMory:LOAD<n>:TFACtor \n
		Snippet: driver.massMemory.load.tfactor.set(filename = '1', window = repcap.Window.Default) \n
		Loads the transducer factor from the selected file in .CSV format. \n
			:param filename: String containing the path and name of the CSV import file.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Load')
		"""
		param = Conversions.value_to_quoted_str(filename)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'MMEMory:LOAD{window_cmd_val}:TFACtor {param}')

	def get(self, window=repcap.Window.Default) -> str:
		"""SCPI: MMEMory:LOAD<n>:TFACtor \n
		Snippet: value: str = driver.massMemory.load.tfactor.get(window = repcap.Window.Default) \n
		Loads the transducer factor from the selected file in .CSV format. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Load')
			:return: filename: String containing the path and name of the CSV import file."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'MMEMory:LOAD{window_cmd_val}:TFACtor?')
		return trim_str_response(response)
