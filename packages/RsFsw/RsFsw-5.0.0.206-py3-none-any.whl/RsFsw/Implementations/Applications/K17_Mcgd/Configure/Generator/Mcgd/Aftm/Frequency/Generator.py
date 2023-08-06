from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Generator:
	"""Generator commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("generator", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: CONFigure:GENerator:MCGD:AFTM:FREQuency:GENerator \n
		Snippet: driver.applications.k17Mcgd.configure.generator.mcgd.aftm.frequency.generator.set(frequency = 1.0) \n
		Determines the signal generator frequency. Any changes here are automatically applied to the connected generator. \n
			:param frequency: Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'CONFigure:GENerator:MCGD:AFTM:FREQuency:GENerator {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:GENerator:MCGD:AFTM:FREQuency:GENerator \n
		Snippet: value: float = driver.applications.k17Mcgd.configure.generator.mcgd.aftm.frequency.generator.get() \n
		Determines the signal generator frequency. Any changes here are automatically applied to the connected generator. \n
			:return: frequency: Unit: HZ"""
		response = self._core.io.query_str(f'CONFigure:GENerator:MCGD:AFTM:FREQuency:GENerator?')
		return Conversions.str_to_float(response)
