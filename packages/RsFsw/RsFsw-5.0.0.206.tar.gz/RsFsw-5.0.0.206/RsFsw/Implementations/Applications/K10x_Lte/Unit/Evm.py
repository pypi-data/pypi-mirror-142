from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Evm:
	"""Evm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("evm", core, parent)

	def set(self, unit: enums.UnitMode) -> None:
		"""SCPI: UNIT:EVM \n
		Snippet: driver.applications.k10Xlte.unit.evm.set(unit = enums.UnitMode.DB) \n
		This command selects the EVM unit. \n
			:param unit: DB EVM results returned in dB PCT EVM results returned in %
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.UnitMode)
		self._core.io.write(f'UNIT:EVM {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.UnitMode:
		"""SCPI: UNIT:EVM \n
		Snippet: value: enums.UnitMode = driver.applications.k10Xlte.unit.evm.get() \n
		This command selects the EVM unit. \n
			:return: unit: DB EVM results returned in dB PCT EVM results returned in %"""
		response = self._core.io.query_str(f'UNIT:EVM?')
		return Conversions.str_to_scalar_enum(response, enums.UnitMode)
