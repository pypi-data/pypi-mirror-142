from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Unit:
	"""Unit commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("unit", core, parent)

	def set(self, unit: enums.UnitMode) -> None:
		"""SCPI: CONFigure:ADEMod:RESults:UNIT \n
		Snippet: driver.configure.ademod.results.unit.set(unit = enums.UnitMode.DB) \n
		This command selects the unit for relative demodulation results. \n
			:param unit: PCT | DB
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.UnitMode)
		self._core.io.write(f'CONFigure:ADEMod:RESults:UNIT {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.UnitMode:
		"""SCPI: CONFigure:ADEMod:RESults:UNIT \n
		Snippet: value: enums.UnitMode = driver.configure.ademod.results.unit.get() \n
		This command selects the unit for relative demodulation results. \n
			:return: unit: PCT | DB"""
		response = self._core.io.query_str(f'CONFigure:ADEMod:RESults:UNIT?')
		return Conversions.str_to_scalar_enum(response, enums.UnitMode)
