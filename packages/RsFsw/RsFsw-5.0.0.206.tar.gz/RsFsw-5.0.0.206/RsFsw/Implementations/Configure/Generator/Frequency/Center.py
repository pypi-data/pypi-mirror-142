from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Center:
	"""Center commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("center", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: CONFigure:GENerator:FREQuency:CENTer \n
		Snippet: driver.configure.generator.frequency.center.set(frequency = 1.0) \n
		Defines the frequency of the signal provided by the signal generator. \n
			:param frequency: Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'CONFigure:GENerator:FREQuency:CENTer {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:GENerator:FREQuency:CENTer \n
		Snippet: value: float = driver.configure.generator.frequency.center.get() \n
		Defines the frequency of the signal provided by the signal generator. \n
			:return: frequency: Unit: HZ"""
		response = self._core.io.query_str(f'CONFigure:GENerator:FREQuency:CENTer?')
		return Conversions.str_to_float(response)
