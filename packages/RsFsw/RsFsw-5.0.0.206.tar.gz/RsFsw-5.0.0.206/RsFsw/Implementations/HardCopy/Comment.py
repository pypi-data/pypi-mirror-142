from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Comment:
	"""Comment commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("comment", core, parent)

	def set(self, arg_0: str) -> None:
		"""SCPI: HCOPy:COMMent \n
		Snippet: driver.hardCopy.comment.set(arg_0 = '1') \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.value_to_quoted_str(arg_0)
		self._core.io.write(f'HCOPy:COMMent {param}')

	def get(self) -> str:
		"""SCPI: HCOPy:COMMent \n
		Snippet: value: str = driver.hardCopy.comment.get() \n
		No command help available \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'HCOPy:COMMent?')
		return trim_str_response(response)
