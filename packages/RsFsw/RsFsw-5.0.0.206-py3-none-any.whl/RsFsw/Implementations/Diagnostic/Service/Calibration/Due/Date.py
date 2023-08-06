from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Date:
	"""Date commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("date", core, parent)

	def set(self, date: str) -> None:
		"""SCPI: DIAGnostic:SERVice:CALibration:DUE:DATE \n
		Snippet: driver.diagnostic.service.calibration.due.date.set(date = '1') \n
		This command sets next date and time the instrument needs calibration to be done in ISO 8601 format. The response may be
		empty in case of no fixed next calibration due. \n
			:param date: String containing next calibration due date. An empty string resets the date (= no due date) .
		"""
		param = Conversions.value_to_quoted_str(date)
		self._core.io.write(f'DIAGnostic:SERVice:CALibration:DUE:DATE {param}')

	def get(self) -> str:
		"""SCPI: DIAGnostic:SERVice:CALibration:DUE:DATE \n
		Snippet: value: str = driver.diagnostic.service.calibration.due.date.get() \n
		This command sets next date and time the instrument needs calibration to be done in ISO 8601 format. The response may be
		empty in case of no fixed next calibration due. \n
			:return: date: No help available"""
		response = self._core.io.query_str(f'DIAGnostic:SERVice:CALibration:DUE:DATE?')
		return trim_str_response(response)
