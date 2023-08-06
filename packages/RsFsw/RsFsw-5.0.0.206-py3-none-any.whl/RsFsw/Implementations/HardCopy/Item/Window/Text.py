from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Text:
	"""Text commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("text", core, parent)

	def set(self, comment: str, window=repcap.Window.Default) -> None:
		"""SCPI: HCOPy:ITEM:WINDow<1|2>:TEXT \n
		Snippet: driver.hardCopy.item.window.text.set(comment = '1', window = repcap.Window.Default) \n
		This command defines a comment to be added to the printout. \n
			:param comment: String containing the comment.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.value_to_quoted_str(comment)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'HCOPy:ITEM:WINDow{window_cmd_val}:TEXT {param}')

	def get(self, window=repcap.Window.Default) -> str:
		"""SCPI: HCOPy:ITEM:WINDow<1|2>:TEXT \n
		Snippet: value: str = driver.hardCopy.item.window.text.get(window = repcap.Window.Default) \n
		This command defines a comment to be added to the printout. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: comment: String containing the comment."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'HCOPy:ITEM:WINDow{window_cmd_val}:TEXT?')
		return trim_str_response(response)
