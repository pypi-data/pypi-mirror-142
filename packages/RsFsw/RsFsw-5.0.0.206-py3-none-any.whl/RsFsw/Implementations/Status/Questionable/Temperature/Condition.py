from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Condition:
	"""Condition commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("condition", core, parent)

	def get(self) -> str:
		"""SCPI: STATus:QUEStionable:TEMPerature:CONDition \n
		Snippet: value: str = driver.status.questionable.temperature.condition.get() \n
		These commands read out the CONDition section of the status register. The commands do not delete the contents of the
		CONDition section. \n
			:return: channel_name: String containing the name of the channel. The parameter is optional. If you omit it, the command works for the currently active channel."""
		response = self._core.io.query_str(f'STATus:QUEStionable:TEMPerature:CONDition?')
		return trim_str_response(response)
