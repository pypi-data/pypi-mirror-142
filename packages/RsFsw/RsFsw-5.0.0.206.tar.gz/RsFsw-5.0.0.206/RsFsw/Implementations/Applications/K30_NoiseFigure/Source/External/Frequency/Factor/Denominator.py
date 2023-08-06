from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Denominator:
	"""Denominator commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("denominator", core, parent)

	def set(self, denominator: float) -> None:
		"""SCPI: SOURce:EXTernal:FREQuency[:FACTor]:DENominator \n
		Snippet: driver.applications.k30NoiseFigure.source.external.frequency.factor.denominator.set(denominator = 1.0) \n
		No command help available \n
			:param denominator: Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(denominator)
		self._core.io.write(f'SOURce:EXTernal:FREQuency:FACTor:DENominator {param}')

	def get(self) -> float:
		"""SCPI: SOURce:EXTernal:FREQuency[:FACTor]:DENominator \n
		Snippet: value: float = driver.applications.k30NoiseFigure.source.external.frequency.factor.denominator.get() \n
		No command help available \n
			:return: denominator: Unit: HZ"""
		response = self._core.io.query_str(f'SOURce:EXTernal:FREQuency:FACTor:DENominator?')
		return Conversions.str_to_float(response)
