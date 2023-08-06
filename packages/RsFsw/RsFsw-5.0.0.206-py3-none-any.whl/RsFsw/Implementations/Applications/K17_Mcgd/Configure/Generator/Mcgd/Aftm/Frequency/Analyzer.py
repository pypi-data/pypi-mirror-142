from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Analyzer:
	"""Analyzer commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("analyzer", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: CONFigure:GENerator:MCGD:AFTM:FREQuency:ANALyzer \n
		Snippet: driver.applications.k17Mcgd.configure.generator.mcgd.aftm.frequency.analyzer.set(frequency = 1.0) \n
		Sets or queries the analyzer frequency for the frequency translating measurement. During the group delay measurement,
		this value corresponds to the center frequency of the R&S FSW MCGD application. \n
			:param frequency: Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'CONFigure:GENerator:MCGD:AFTM:FREQuency:ANALyzer {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:GENerator:MCGD:AFTM:FREQuency:ANALyzer \n
		Snippet: value: float = driver.applications.k17Mcgd.configure.generator.mcgd.aftm.frequency.analyzer.get() \n
		Sets or queries the analyzer frequency for the frequency translating measurement. During the group delay measurement,
		this value corresponds to the center frequency of the R&S FSW MCGD application. \n
			:return: frequency: Unit: HZ"""
		response = self._core.io.query_str(f'CONFigure:GENerator:MCGD:AFTM:FREQuency:ANALyzer?')
		return Conversions.str_to_float(response)
