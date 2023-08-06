from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.Utilities import trim_str_response
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Condition:
	"""Condition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("condition", core, parent)

	def get(self, window=repcap.Window.Default) -> str:
		"""SCPI: STATus:QUEStionable:MODulation<Window>:IQRHo:CONDition \n
		Snippet: value: str = driver.applications.k70Vsa.status.questionable.modulation.iqRho.condition.get(window = repcap.Window.Default) \n
		This command reads out the CONDition section of the status register. The command does not delete the contents of the
		EVENt section. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Modulation')
			:return: channel_name: String containing the name of the channel. The parameter is optional. If you omit it, the command works for the currently active channel."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'STATus:QUEStionable:MODulation{window_cmd_val}:IQRHo:CONDition?')
		return trim_str_response(response)
