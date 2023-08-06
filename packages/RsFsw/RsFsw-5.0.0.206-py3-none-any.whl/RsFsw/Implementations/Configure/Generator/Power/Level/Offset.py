from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, level_offset: float) -> None:
		"""SCPI: CONFigure:GENerator:POWer:LEVel:OFFSet \n
		Snippet: driver.configure.generator.power.level.offset.set(level_offset = 1.0) \n
		Defines a fixed offset in the power level used by the generator, for example due to a gain from the DUT. \n
			:param level_offset: numeric value Unit: DBM
		"""
		param = Conversions.decimal_value_to_str(level_offset)
		self._core.io.write(f'CONFigure:GENerator:POWer:LEVel:OFFSet {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:GENerator:POWer:LEVel:OFFSet \n
		Snippet: value: float = driver.configure.generator.power.level.offset.get() \n
		Defines a fixed offset in the power level used by the generator, for example due to a gain from the DUT. \n
			:return: level_offset: numeric value Unit: DBM"""
		response = self._core.io.query_str(f'CONFigure:GENerator:POWer:LEVel:OFFSet?')
		return Conversions.str_to_float(response)
