from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tcase:
	"""Tcase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tcase", core, parent)

	def set(self, test_case: str) -> None:
		"""SCPI: CONFigure[:LTE]:ORAN:TCASe \n
		Snippet: driver.applications.k10Xlte.configure.lte.oran.tcase.set(test_case = '1') \n
		No command help available \n
			:param test_case: No help available
		"""
		param = Conversions.value_to_quoted_str(test_case)
		self._core.io.write(f'CONFigure:LTE:ORAN:TCASe {param}')

	def get(self) -> str:
		"""SCPI: CONFigure[:LTE]:ORAN:TCASe \n
		Snippet: value: str = driver.applications.k10Xlte.configure.lte.oran.tcase.get() \n
		No command help available \n
			:return: test_case: No help available"""
		response = self._core.io.query_str(f'CONFigure:LTE:ORAN:TCASe?')
		return trim_str_response(response)
