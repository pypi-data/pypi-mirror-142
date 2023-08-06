from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Numerator:
	"""Numerator commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("numerator", core, parent)

	def set(self, numerator: float) -> None:
		"""SCPI: CONFigure:GENerator:MCGD:AFTM:FREQuency[:FACTor]:NUMerator \n
		Snippet: driver.applications.k17Mcgd.configure.generator.mcgd.aftm.frequency.factor.numerator.set(numerator = 1.0) \n
		Defines the numerator of the frequency translating factor of the DUT. \n
			:param numerator: No help available
		"""
		param = Conversions.decimal_value_to_str(numerator)
		self._core.io.write(f'CONFigure:GENerator:MCGD:AFTM:FREQuency:FACTor:NUMerator {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:GENerator:MCGD:AFTM:FREQuency[:FACTor]:NUMerator \n
		Snippet: value: float = driver.applications.k17Mcgd.configure.generator.mcgd.aftm.frequency.factor.numerator.get() \n
		Defines the numerator of the frequency translating factor of the DUT. \n
			:return: numerator: No help available"""
		response = self._core.io.query_str(f'CONFigure:GENerator:MCGD:AFTM:FREQuency:FACTor:NUMerator?')
		return Conversions.str_to_float(response)
