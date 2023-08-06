from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Condition:
	"""Condition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("condition", core, parent)

	def get(self, window=repcap.Window.Default) -> str:
		"""SCPI: STATus:QUEStionable:LIMit<1|2|3|4>:CONDition \n
		Snippet: value: str = driver.status.questionable.limit.condition.get(window = repcap.Window.Default) \n
		These commands read out the CONDition section of the status register. The commands do not delete the contents of the
		CONDition section. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: channel_name: String containing the name of the channel. The parameter is optional. If you omit it, the command works for the currently active channel."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'STATus:QUEStionable:LIMit{window_cmd_val}:CONDition?')
		return trim_str_response(response)
