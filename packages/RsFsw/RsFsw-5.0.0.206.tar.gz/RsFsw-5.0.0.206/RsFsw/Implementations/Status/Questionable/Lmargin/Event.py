from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Event:
	"""Event commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("event", core, parent)

	def get(self, window=repcap.Window.Default) -> str:
		"""SCPI: STATus:QUEStionable:LMARgin<1|2|3|4>[:EVENt] \n
		Snippet: value: str = driver.status.questionable.lmargin.event.get(window = repcap.Window.Default) \n
		These commands read out the EVENt section of the status register. At the same time, the commands delete the contents of
		the EVENt section. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Lmargin')
			:return: channel_name: String containing the name of the channel. The parameter is optional. If you omit it, the command works for the currently active channel."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'STATus:QUEStionable:LMARgin{window_cmd_val}:EVENt?')
		return trim_str_response(response)
