from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gimbalance:
	"""Gimbalance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gimbalance", core, parent)

	def set(self, unit: enums.UnitMode) -> None:
		"""SCPI: UNIT:GIMBalance \n
		Snippet: driver.applications.k91Wlan.unit.gimbalance.set(unit = enums.UnitMode.DB) \n
		This command specifies the units for gain imbalance results For details see 'Modulation accuracy, flatness and tolerance
		parameters'. \n
			:param unit: DB | PCT
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.UnitMode)
		self._core.io.write(f'UNIT:GIMBalance {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.UnitMode:
		"""SCPI: UNIT:GIMBalance \n
		Snippet: value: enums.UnitMode = driver.applications.k91Wlan.unit.gimbalance.get() \n
		This command specifies the units for gain imbalance results For details see 'Modulation accuracy, flatness and tolerance
		parameters'. \n
			:return: unit: DB | PCT"""
		response = self._core.io.query_str(f'UNIT:GIMBalance?')
		return Conversions.str_to_scalar_enum(response, enums.UnitMode)
