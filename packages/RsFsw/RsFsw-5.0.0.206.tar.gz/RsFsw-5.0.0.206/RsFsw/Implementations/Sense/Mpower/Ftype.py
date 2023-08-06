from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ftype:
	"""Ftype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ftype", core, parent)

	def set(self, filter_type: enums.FilterTypeC) -> None:
		"""SCPI: [SENSe]:MPOWer:FTYPe \n
		Snippet: driver.sense.mpower.ftype.set(filter_type = enums.FilterTypeC.CFILter) \n
		This command selects the filter type for pulse power measurements. The EMI-specific filter types are available if the EMI
		(R&S FSW-K54) measurement option is installed, even if EMI measurement is not active. For details see 'Resolution
		bandwidth and filter types'. \n
			:param filter_type: CFILter NORMal P5 RRC CISPr | PULSe CISPR (6 dB) - requires EMI (R&S FSW-K54) option Return value for query is always PULS. MIL MIL Std (6 dB) - requires EMI (R&S FSW-K54) option
		"""
		param = Conversions.enum_scalar_to_str(filter_type, enums.FilterTypeC)
		self._core.io.write(f'SENSe:MPOWer:FTYPe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FilterTypeC:
		"""SCPI: [SENSe]:MPOWer:FTYPe \n
		Snippet: value: enums.FilterTypeC = driver.sense.mpower.ftype.get() \n
		This command selects the filter type for pulse power measurements. The EMI-specific filter types are available if the EMI
		(R&S FSW-K54) measurement option is installed, even if EMI measurement is not active. For details see 'Resolution
		bandwidth and filter types'. \n
			:return: filter_type: CFILter NORMal P5 RRC CISPr | PULSe CISPR (6 dB) - requires EMI (R&S FSW-K54) option Return value for query is always PULS. MIL MIL Std (6 dB) - requires EMI (R&S FSW-K54) option"""
		response = self._core.io.query_str(f'SENSe:MPOWer:FTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.FilterTypeC)
