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

	def set(self, unit: enums.PageMarginUnit) -> None:
		"""SCPI: HCOPy:PAGE:MARGin:UNIT \n
		Snippet: driver.hardCopy.page.margin.unit.set(unit = enums.PageMarginUnit.IN) \n
		This command defines the unit in which the margins for the printout page are configured. \n
			:param unit: MM | IN MM millimeters IN inches
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.PageMarginUnit)
		self._core.io.write(f'HCOPy:PAGE:MARGin:UNIT {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PageMarginUnit:
		"""SCPI: HCOPy:PAGE:MARGin:UNIT \n
		Snippet: value: enums.PageMarginUnit = driver.hardCopy.page.margin.unit.get() \n
		This command defines the unit in which the margins for the printout page are configured. \n
			:return: unit: MM | IN MM millimeters IN inches"""
		response = self._core.io.query_str(f'HCOPy:PAGE:MARGin:UNIT?')
		return Conversions.str_to_scalar_enum(response, enums.PageMarginUnit)
