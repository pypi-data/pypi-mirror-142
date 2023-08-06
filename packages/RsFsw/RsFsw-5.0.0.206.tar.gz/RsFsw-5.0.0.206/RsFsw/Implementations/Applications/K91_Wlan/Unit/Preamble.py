from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Preamble:
	"""Preamble commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("preamble", core, parent)

	def set(self, unit: enums.PreambleUnit) -> None:
		"""SCPI: UNIT:PREamble \n
		Snippet: driver.applications.k91Wlan.unit.preamble.set(unit = enums.PreambleUnit.HZ) \n
		This command specifies the units for preamble error results. \n
			:param unit: HZ | PCT
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.PreambleUnit)
		self._core.io.write(f'UNIT:PREamble {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PreambleUnit:
		"""SCPI: UNIT:PREamble \n
		Snippet: value: enums.PreambleUnit = driver.applications.k91Wlan.unit.preamble.get() \n
		This command specifies the units for preamble error results. \n
			:return: unit: HZ | PCT"""
		response = self._core.io.query_str(f'UNIT:PREamble?')
		return Conversions.str_to_scalar_enum(response, enums.PreambleUnit)
