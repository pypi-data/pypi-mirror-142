from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Event:
	"""Event commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("event", core, parent)

	def get(self) -> str:
		"""SCPI: STATus:QUEStionable:PNOise[:EVENt] \n
		Snippet: value: str = driver.status.questionable.pnoise.event.get() \n
		No command help available \n
			:return: channel_name: No help available"""
		response = self._core.io.query_str(f'STATus:QUEStionable:PNOise:EVENt?')
		return trim_str_response(response)
