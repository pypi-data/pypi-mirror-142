from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Denominator:
	"""Denominator commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("denominator", core, parent)

	def set(self, denominator: float) -> None:
		"""SCPI: CONFigure:GENerator:MCGD:AFTM:FREQuency[:FACTor]:DENominator \n
		Snippet: driver.applications.k17Mcgd.configure.generator.mcgd.aftm.frequency.factor.denominator.set(denominator = 1.0) \n
		Defines the denominator of the frequency translating factor of the DUT. \n
			:param denominator: No help available
		"""
		param = Conversions.decimal_value_to_str(denominator)
		self._core.io.write(f'CONFigure:GENerator:MCGD:AFTM:FREQuency:FACTor:DENominator {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:GENerator:MCGD:AFTM:FREQuency[:FACTor]:DENominator \n
		Snippet: value: float = driver.applications.k17Mcgd.configure.generator.mcgd.aftm.frequency.factor.denominator.get() \n
		Defines the denominator of the frequency translating factor of the DUT. \n
			:return: denominator: No help available"""
		response = self._core.io.query_str(f'CONFigure:GENerator:MCGD:AFTM:FREQuency:FACTor:DENominator?')
		return Conversions.str_to_float(response)
