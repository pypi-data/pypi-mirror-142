from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Numerator:
	"""Numerator commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("numerator", core, parent)

	def set(self, numerator: float) -> None:
		"""SCPI: SOURce:EXTernal:FREQuency[:FACTor]:NUMerator \n
		Snippet: driver.applications.k30NoiseFigure.source.external.frequency.factor.numerator.set(numerator = 1.0) \n
		No command help available \n
			:param numerator: No help available
		"""
		param = Conversions.decimal_value_to_str(numerator)
		self._core.io.write(f'SOURce:EXTernal:FREQuency:FACTor:NUMerator {param}')

	def get(self) -> float:
		"""SCPI: SOURce:EXTernal:FREQuency[:FACTor]:NUMerator \n
		Snippet: value: float = driver.applications.k30NoiseFigure.source.external.frequency.factor.numerator.get() \n
		No command help available \n
			:return: numerator: No help available"""
		response = self._core.io.query_str(f'SOURce:EXTernal:FREQuency:FACTor:NUMerator?')
		return Conversions.str_to_float(response)
