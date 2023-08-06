from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: SOURce:GENerator:FREQuency \n
		Snippet: driver.applications.k30NoiseFigure.source.generator.frequency.set(frequency = 1.0) \n
		No command help available \n
			:param frequency: No help available
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SOURce:GENerator:FREQuency {param}')

	def get(self) -> float:
		"""SCPI: SOURce:GENerator:FREQuency \n
		Snippet: value: float = driver.applications.k30NoiseFigure.source.generator.frequency.get() \n
		No command help available \n
			:return: frequency: No help available"""
		response = self._core.io.query_str(f'SOURce:GENerator:FREQuency?')
		return Conversions.str_to_float(response)
