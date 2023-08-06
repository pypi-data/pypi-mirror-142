from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Caxes:
	"""Caxes commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("caxes", core, parent)

	def set(self, unit: enums.LimitUnitLte) -> None:
		"""SCPI: UNIT:CAXes \n
		Snippet: driver.applications.k10Xlte.unit.caxes.set(unit = enums.LimitUnitLte.CARR) \n
		This command selects the scale of the x-axis for result displays that show subcarrier results. \n
			:param unit: CARR Shows the number of the subcarriers on the x-axis. HZ Shows the frequency of the subcarriers on the x-axis.
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.LimitUnitLte)
		self._core.io.write(f'UNIT:CAXes {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.LimitUnitLte:
		"""SCPI: UNIT:CAXes \n
		Snippet: value: enums.LimitUnitLte = driver.applications.k10Xlte.unit.caxes.get() \n
		This command selects the scale of the x-axis for result displays that show subcarrier results. \n
			:return: unit: CARR Shows the number of the subcarriers on the x-axis. HZ Shows the frequency of the subcarriers on the x-axis."""
		response = self._core.io.query_str(f'UNIT:CAXes?')
		return Conversions.str_to_scalar_enum(response, enums.LimitUnitLte)
