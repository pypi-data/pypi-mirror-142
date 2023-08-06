from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Numerator:
	"""Numerator commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("numerator", core, parent)

	def set(self, numerator: float) -> None:
		"""SCPI: CONFigure:GENerator:NPRatio:FREQuency[:FACTor]:NUMerator \n
		Snippet: driver.configure.generator.npratio.frequency.factor.numerator.set(numerator = 1.0) \n
		Defines the numerator of the frequency-defining factor for the generator frequency (see 'fGen') . \n
			:param numerator: numeric value
		"""
		param = Conversions.decimal_value_to_str(numerator)
		self._core.io.write(f'CONFigure:GENerator:NPRatio:FREQuency:FACTor:NUMerator {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:GENerator:NPRatio:FREQuency[:FACTor]:NUMerator \n
		Snippet: value: float = driver.configure.generator.npratio.frequency.factor.numerator.get() \n
		Defines the numerator of the frequency-defining factor for the generator frequency (see 'fGen') . \n
			:return: numerator: numeric value"""
		response = self._core.io.query_str(f'CONFigure:GENerator:NPRatio:FREQuency:FACTor:NUMerator?')
		return Conversions.str_to_float(response)
