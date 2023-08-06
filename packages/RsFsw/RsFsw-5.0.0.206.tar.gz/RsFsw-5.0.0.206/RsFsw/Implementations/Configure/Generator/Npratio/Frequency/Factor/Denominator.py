from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Denominator:
	"""Denominator commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("denominator", core, parent)

	def set(self, denominator: float) -> None:
		"""SCPI: CONFigure:GENerator:NPRatio:FREQuency[:FACTor]:DENominator \n
		Snippet: driver.configure.generator.npratio.frequency.factor.denominator.set(denominator = 1.0) \n
		Defines the denominator of the frequency-defining factor for the generator frequency (see 'fGen') . \n
			:param denominator: numeric value
		"""
		param = Conversions.decimal_value_to_str(denominator)
		self._core.io.write(f'CONFigure:GENerator:NPRatio:FREQuency:FACTor:DENominator {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:GENerator:NPRatio:FREQuency[:FACTor]:DENominator \n
		Snippet: value: float = driver.configure.generator.npratio.frequency.factor.denominator.get() \n
		Defines the denominator of the frequency-defining factor for the generator frequency (see 'fGen') . \n
			:return: denominator: numeric value"""
		response = self._core.io.query_str(f'CONFigure:GENerator:NPRatio:FREQuency:FACTor:DENominator?')
		return Conversions.str_to_float(response)
