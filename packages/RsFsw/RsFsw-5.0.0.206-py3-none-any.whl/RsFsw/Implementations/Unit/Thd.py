from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Thd:
	"""Thd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("thd", core, parent)

	def set(self, mode: enums.UnitMode) -> None:
		"""SCPI: UNIT:THD \n
		Snippet: driver.unit.thd.set(mode = enums.UnitMode.DB) \n
		Selects the unit for THD measurements (<n> is irrelevant) . This command is identical to CALC:UNIT:THD \n
			:param mode: DB | PCT
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.UnitMode)
		self._core.io.write(f'UNIT:THD {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.UnitMode:
		"""SCPI: UNIT:THD \n
		Snippet: value: enums.UnitMode = driver.unit.thd.get() \n
		Selects the unit for THD measurements (<n> is irrelevant) . This command is identical to CALC:UNIT:THD \n
			:return: mode: DB | PCT"""
		response = self._core.io.query_str(f'UNIT:THD?')
		return Conversions.str_to_scalar_enum(response, enums.UnitMode)
