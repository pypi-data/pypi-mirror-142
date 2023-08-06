from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tcase:
	"""Tcase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tcase", core, parent)

	def set(self, test_case: enums.TestCaseNr5G) -> None:
		"""SCPI: CONFigure[:NR5G]:ORAN:TCASe \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.oran.tcase.set(test_case = enums.TestCaseNr5G.NONE) \n
		No command help available \n
			:param test_case: (enum or string) No help available
		"""
		param = Conversions.enum_ext_scalar_to_str(test_case, enums.TestCaseNr5G)
		self._core.io.write(f'CONFigure:NR5G:ORAN:TCASe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.TestCaseNr5G:
		"""SCPI: CONFigure[:NR5G]:ORAN:TCASe \n
		Snippet: value: enums.TestCaseNr5G = driver.applications.k14Xnr5G.configure.nr5G.oran.tcase.get() \n
		No command help available \n
			:return: test_case: (enum or string) No help available"""
		response = self._core.io.query_str(f'CONFigure:NR5G:ORAN:TCASe?')
		return Conversions.str_to_scalar_enum_ext(response, enums.TestCaseNr5G)
