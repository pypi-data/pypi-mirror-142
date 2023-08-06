from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Comment:
	"""Comment commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("comment", core, parent)

	def set(self, comment: str, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:MASK:COMMent \n
		Snippet: driver.calculate.mask.comment.set(comment = '1', window = repcap.Window.Default) \n
		This command defines a comment for the frequency mask that you have selected with method RsFsw.Calculate.Mask.Name.set. \n
			:param comment: String containing the comment for the frequency mask.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.value_to_quoted_str(comment)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:MASK:COMMent {param}')

	def get(self, window=repcap.Window.Default) -> str:
		"""SCPI: CALCulate<n>:MASK:COMMent \n
		Snippet: value: str = driver.calculate.mask.comment.get(window = repcap.Window.Default) \n
		This command defines a comment for the frequency mask that you have selected with method RsFsw.Calculate.Mask.Name.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: comment: String containing the comment for the frequency mask."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MASK:COMMent?')
		return trim_str_response(response)
