from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Catalog:
	"""Catalog commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("catalog", core, parent)

	def set(self, patterns: enums.SelectionRangeB) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:CATalog \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.sync.catalog.set(patterns = enums.SelectionRangeB.ALL) \n
		This command reads the names of all patterns stored on the hard disk. The file names are returned as a comma-separated
		list of strings, one for each file name (without the file extension) . \n
			:param patterns: CURRent | ALL CURRent Only patterns that belong to the current standard ALL All patterns
		"""
		param = Conversions.enum_scalar_to_str(patterns, enums.SelectionRangeB)
		self._core.io.write(f'SENSe:DDEMod:SEARch:SYNC:CATalog {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SelectionRangeB:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:CATalog \n
		Snippet: value: enums.SelectionRangeB = driver.applications.k70Vsa.sense.ddemod.search.sync.catalog.get() \n
		This command reads the names of all patterns stored on the hard disk. The file names are returned as a comma-separated
		list of strings, one for each file name (without the file extension) . \n
			:return: patterns: CURRent | ALL CURRent Only patterns that belong to the current standard ALL All patterns"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SEARch:SYNC:CATalog?')
		return Conversions.str_to_scalar_enum(response, enums.SelectionRangeB)
