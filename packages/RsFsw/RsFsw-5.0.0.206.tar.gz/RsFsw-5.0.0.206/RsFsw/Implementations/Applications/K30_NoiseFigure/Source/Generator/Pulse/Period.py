from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Period:
	"""Period commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("period", core, parent)

	def set(self, pulse_period: float) -> None:
		"""SCPI: SOURce:GENerator:PULSe:PERiod \n
		Snippet: driver.applications.k30NoiseFigure.source.generator.pulse.period.set(pulse_period = 1.0) \n
		No command help available \n
			:param pulse_period: No help available
		"""
		param = Conversions.decimal_value_to_str(pulse_period)
		self._core.io.write(f'SOURce:GENerator:PULSe:PERiod {param}')

	def get(self) -> float:
		"""SCPI: SOURce:GENerator:PULSe:PERiod \n
		Snippet: value: float = driver.applications.k30NoiseFigure.source.generator.pulse.period.get() \n
		No command help available \n
			:return: pulse_period: No help available"""
		response = self._core.io.query_str(f'SOURce:GENerator:PULSe:PERiod?')
		return Conversions.str_to_float(response)
