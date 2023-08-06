from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bstream:
	"""Bstream commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bstream", core, parent)

	def set(self, unit: enums.BstreamUnit) -> None:
		"""SCPI: UNIT:BSTReam \n
		Snippet: driver.applications.k14Xnr5G.unit.bstream.set(unit = enums.BstreamUnit.BIT) \n
		This command selects the way the bit stream is displayed. \n
			:param unit: SYMbols Displays the bit stream using symbols BITs Displays the bit stream using bits
		"""
		param = Conversions.enum_scalar_to_str(unit, enums.BstreamUnit)
		self._core.io.write(f'UNIT:BSTReam {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.BstreamUnit:
		"""SCPI: UNIT:BSTReam \n
		Snippet: value: enums.BstreamUnit = driver.applications.k14Xnr5G.unit.bstream.get() \n
		This command selects the way the bit stream is displayed. \n
			:return: unit: SYMbols Displays the bit stream using symbols BITs Displays the bit stream using bits"""
		response = self._core.io.query_str(f'UNIT:BSTReam?')
		return Conversions.str_to_scalar_enum(response, enums.BstreamUnit)
