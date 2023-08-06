from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Date:
	"""Date commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("date", core, parent)

	def set(self, date: str) -> None:
		"""SCPI: DIAGnostic:SERVice:DATE \n
		Snippet: driver.diagnostic.service.date.set(date = '1') \n
		This command sets the last date and time the instrument was serviced (ISO 8601 format) . \n
			:param date: String containing last service date.
		"""
		param = Conversions.value_to_quoted_str(date)
		self._core.io.write(f'DIAGnostic:SERVice:DATE {param}')

	def get(self) -> str:
		"""SCPI: DIAGnostic:SERVice:DATE \n
		Snippet: value: str = driver.diagnostic.service.date.get() \n
		This command sets the last date and time the instrument was serviced (ISO 8601 format) . \n
			:return: date: No help available"""
		response = self._core.io.query_str(f'DIAGnostic:SERVice:DATE?')
		return trim_str_response(response)
