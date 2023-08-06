from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Width:
	"""Width commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("width", core, parent)

	def set(self, pulse_width: float) -> None:
		"""SCPI: SOURce:GENerator:PULSe:WIDTh \n
		Snippet: driver.applications.k30NoiseFigure.source.generator.pulse.width.set(pulse_width = 1.0) \n
		No command help available \n
			:param pulse_width: No help available
		"""
		param = Conversions.decimal_value_to_str(pulse_width)
		self._core.io.write(f'SOURce:GENerator:PULSe:WIDTh {param}')

	def get(self) -> float:
		"""SCPI: SOURce:GENerator:PULSe:WIDTh \n
		Snippet: value: float = driver.applications.k30NoiseFigure.source.generator.pulse.width.get() \n
		No command help available \n
			:return: pulse_width: No help available"""
		response = self._core.io.query_str(f'SOURce:GENerator:PULSe:WIDTh?')
		return Conversions.str_to_float(response)
