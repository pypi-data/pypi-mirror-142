from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Saxes:
	"""Saxes commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("saxes", core, parent)

	def set(self, unit: enums.XaxisUnitScale) -> None:
		"""SCPI: UNIT:SAXes \n
		Snippet: driver.applications.k14Xnr5G.unit.saxes.set(unit = enums.XaxisUnitScale.SYMBol) \n
		This command selects the scale of the x-axis for result displays that show symbol results. \n
			:param unit: SYMBol Shows the number of the symbol on the x-axis. TIME Shows the time stamp of the symbols on the x-axis.
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.XaxisUnitScale)
		self._core.io.write(f'UNIT:SAXes {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.XaxisUnitScale:
		"""SCPI: UNIT:SAXes \n
		Snippet: value: enums.XaxisUnitScale = driver.applications.k14Xnr5G.unit.saxes.get() \n
		This command selects the scale of the x-axis for result displays that show symbol results. \n
			:return: unit: SYMBol Shows the number of the symbol on the x-axis. TIME Shows the time stamp of the symbols on the x-axis."""
		response = self._core.io.query_str(f'UNIT:SAXes?')
		return Conversions.str_to_scalar_enum(response, enums.XaxisUnitScale)
