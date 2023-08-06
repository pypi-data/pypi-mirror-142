from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, frequency_offset: float) -> None:
		"""SCPI: CONFigure:GENerator:NPRatio:FREQuency:OFFSet \n
		Snippet: driver.configure.generator.npratio.frequency.offset.set(frequency_offset = 1.0) \n
		Defines a fixed offset to be applied to the generator frequency. \n
			:param frequency_offset: numeric value Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(frequency_offset)
		self._core.io.write(f'CONFigure:GENerator:NPRatio:FREQuency:OFFSet {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:GENerator:NPRatio:FREQuency:OFFSet \n
		Snippet: value: float = driver.configure.generator.npratio.frequency.offset.get() \n
		Defines a fixed offset to be applied to the generator frequency. \n
			:return: frequency_offset: numeric value Unit: HZ"""
		response = self._core.io.query_str(f'CONFigure:GENerator:NPRatio:FREQuency:OFFSet?')
		return Conversions.str_to_float(response)
