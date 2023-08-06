from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Event:
	"""Event commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("event", core, parent)

	def get(self) -> int:
		"""SCPI: STATus:QUEStionable[:EVENt] \n
		Snippet: value: int = driver.status.questionable.event.get() \n
		These commands read out the EVENt section of the status register. At the same time, the commands delete the contents of
		the EVENt section. \n
			:return: register_value: No help available"""
		response = self._core.io.query_str(f'STATus:QUEStionable:EVENt?')
		return Conversions.str_to_int(response)
