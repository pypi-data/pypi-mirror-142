from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Angle:
	"""Angle commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("angle", core, parent)

	def set(self, unit: enums.AngleUnit) -> None:
		"""SCPI: UNIT:ANGLe \n
		Snippet: driver.unit.angle.set(unit = enums.AngleUnit.DEG) \n
		This command selects the unit for angles (for PM display, <n> is irrelevant) . This command is identical to method RsFsw.
		Calculate.Unit.Angle.set \n
			:param unit: DEG | RAD
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.AngleUnit)
		self._core.io.write(f'UNIT:ANGLe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AngleUnit:
		"""SCPI: UNIT:ANGLe \n
		Snippet: value: enums.AngleUnit = driver.unit.angle.get() \n
		This command selects the unit for angles (for PM display, <n> is irrelevant) . This command is identical to method RsFsw.
		Calculate.Unit.Angle.set \n
			:return: unit: DEG | RAD"""
		response = self._core.io.query_str(f'UNIT:ANGLe?')
		return Conversions.str_to_scalar_enum(response, enums.AngleUnit)
