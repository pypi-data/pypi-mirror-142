from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bstr:
	"""Bstr commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bstr", core, parent)

	def set(self, unit: enums.BitstreamUnit) -> None:
		"""SCPI: UNIT:BSTR \n
		Snippet: driver.applications.k10Xlte.unit.bstr.set(unit = enums.BitstreamUnit.BIT) \n
		This command selects the way the bit stream is displayed. \n
			:param unit: SYMbols Displays the bit stream using symbols BITs Displays the bit stream using bits
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.BitstreamUnit)
		self._core.io.write(f'UNIT:BSTR {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.BitstreamUnit:
		"""SCPI: UNIT:BSTR \n
		Snippet: value: enums.BitstreamUnit = driver.applications.k10Xlte.unit.bstr.get() \n
		This command selects the way the bit stream is displayed. \n
			:return: unit: SYMbols Displays the bit stream using symbols BITs Displays the bit stream using bits"""
		response = self._core.io.query_str(f'UNIT:BSTR?')
		return Conversions.str_to_scalar_enum(response, enums.BitstreamUnit)
