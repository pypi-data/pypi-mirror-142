from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, frequency: float) -> None:
		"""SCPI: CONFigure:GENerator:MCGD:AFTM:FREQuency:OFFSet \n
		Snippet: driver.applications.k17Mcgd.configure.generator.mcgd.aftm.frequency.offset.set(frequency = 1.0) \n
		Defines a fixed offset to be applied to the generator frequency as an effect of the DUT. \n
			:param frequency: Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'CONFigure:GENerator:MCGD:AFTM:FREQuency:OFFSet {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:GENerator:MCGD:AFTM:FREQuency:OFFSet \n
		Snippet: value: float = driver.applications.k17Mcgd.configure.generator.mcgd.aftm.frequency.offset.get() \n
		Defines a fixed offset to be applied to the generator frequency as an effect of the DUT. \n
			:return: frequency: Unit: HZ"""
		response = self._core.io.query_str(f'CONFigure:GENerator:MCGD:AFTM:FREQuency:OFFSet?')
		return Conversions.str_to_float(response)
