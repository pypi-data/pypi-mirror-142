from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Comment:
	"""Comment commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("comment", core, parent)

	def set(self, comment: str, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:COMMent \n
		Snippet: driver.applications.k30NoiseFigure.calculate.limit.comment.set(comment = '1', window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command defines a comment for a limit line. \n
			:param comment: String containing the description of the limit line.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.value_to_quoted_str(comment)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:COMMent {param}')

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default) -> str:
		"""SCPI: CALCulate<n>:LIMit<li>:COMMent \n
		Snippet: value: str = driver.applications.k30NoiseFigure.calculate.limit.comment.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default) \n
		This command defines a comment for a limit line. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: comment: String containing the description of the limit line."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:COMMent?')
		return trim_str_response(response)
