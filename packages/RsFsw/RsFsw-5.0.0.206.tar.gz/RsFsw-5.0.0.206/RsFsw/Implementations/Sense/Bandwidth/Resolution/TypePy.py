from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, filter_type: enums.FilterTypeB) -> None:
		"""SCPI: [SENSe]:BWIDth[:RESolution]:TYPE \n
		Snippet: driver.sense.bandwidth.resolution.typePy.set(filter_type = enums.FilterTypeB.CFILter) \n
		This command selects the resolution filter type. When you change the filter type, the command selects the next larger
		filter bandwidth if the same bandwidth is unavailable for that filter. The EMI-specific filter types are available if the
		EMI (R&S FSW-K54) measurement option is installed, even if EMI measurement is not active. For details see 'Resolution
		bandwidth and filter types'. \n
			:param filter_type: CFILter Channel filters NORMal Gaussian filters P5 5-pole filters The 5-pole filter is not available for FFT sweeps. RRC RRC filters CISPr | PULSe CISPR (6 dB) - requires EMI (R&S FSW-K54) option Return value for query is always PULS. MIL MIL Std (6 dB) - requires EMI (R&S FSW-K54) option
		"""
		param = Conversions.enum_scalar_to_str(filter_type, enums.FilterTypeB)
		self._core.io.write(f'SENSe:BWIDth:RESolution:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FilterTypeB:
		"""SCPI: [SENSe]:BWIDth[:RESolution]:TYPE \n
		Snippet: value: enums.FilterTypeB = driver.sense.bandwidth.resolution.typePy.get() \n
		This command selects the resolution filter type. When you change the filter type, the command selects the next larger
		filter bandwidth if the same bandwidth is unavailable for that filter. The EMI-specific filter types are available if the
		EMI (R&S FSW-K54) measurement option is installed, even if EMI measurement is not active. For details see 'Resolution
		bandwidth and filter types'. \n
			:return: filter_type: CFILter Channel filters NORMal Gaussian filters P5 5-pole filters The 5-pole filter is not available for FFT sweeps. RRC RRC filters CISPr | PULSe CISPR (6 dB) - requires EMI (R&S FSW-K54) option Return value for query is always PULS. MIL MIL Std (6 dB) - requires EMI (R&S FSW-K54) option"""
		response = self._core.io.query_str(f'SENSe:BWIDth:RESolution:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.FilterTypeB)
