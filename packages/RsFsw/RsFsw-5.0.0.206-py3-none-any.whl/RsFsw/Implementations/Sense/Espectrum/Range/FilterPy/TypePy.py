from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, filter_type: enums.FilterTypeC, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<ri>:FILTer:TYPE \n
		Snippet: driver.sense.espectrum.range.filterPy.typePy.set(filter_type = enums.FilterTypeC.CFILter, subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default) \n
		This command selects the filter type for an SEM range. In case of high speed measurements, the filter has to be identical
		for all ranges. The EMI-specific filter types are available if the EMI (R&S FSW-K54) measurement option is installed,
		even if EMI measurement is not active. For details see 'Resolution bandwidth and filter types'. \n
			:param filter_type: NORMal Gaussian filters CFILter channel filters RRC RRC filters CISPr | PULSe CISPR (6 dB) - requires EMI (R&S FSW-K54) option Return value for query is always PULS. MIL MIL Std (6 dB) - requires EMI (R&S FSW-K54) option P5 5 Pole filters Refer to the datasheet for available filter bandwidths.
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.enum_scalar_to_str(filter_type, enums.FilterTypeC)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:FILTer:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default) -> enums.FilterTypeC:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<ri>:FILTer:TYPE \n
		Snippet: value: enums.FilterTypeC = driver.sense.espectrum.range.filterPy.typePy.get(subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default) \n
		This command selects the filter type for an SEM range. In case of high speed measurements, the filter has to be identical
		for all ranges. The EMI-specific filter types are available if the EMI (R&S FSW-K54) measurement option is installed,
		even if EMI measurement is not active. For details see 'Resolution bandwidth and filter types'. \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:return: filter_type: NORMal Gaussian filters CFILter channel filters RRC RRC filters CISPr | PULSe CISPR (6 dB) - requires EMI (R&S FSW-K54) option Return value for query is always PULS. MIL MIL Std (6 dB) - requires EMI (R&S FSW-K54) option P5 5 Pole filters Refer to the datasheet for available filter bandwidths."""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:FILTer:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.FilterTypeC)
