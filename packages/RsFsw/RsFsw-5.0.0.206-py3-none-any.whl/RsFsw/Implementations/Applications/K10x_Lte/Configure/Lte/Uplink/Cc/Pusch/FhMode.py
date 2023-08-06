from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FhMode:
	"""FhMode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fhMode", core, parent)

	def set(self, hopping_mode: enums.FreqHoppingMode, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PUSCh:FHMode \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.pusch.fhMode.set(hopping_mode = enums.FreqHoppingMode.INTer, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the frequency hopping mode in the PUSCH structure. \n
			:param hopping_mode: NONE No hopping INTer Inter subframe hopping INTRa Intra subframe hopping
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(hopping_mode, enums.FreqHoppingMode)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PUSCh:FHMode {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.FreqHoppingMode:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PUSCh:FHMode \n
		Snippet: value: enums.FreqHoppingMode = driver.applications.k10Xlte.configure.lte.uplink.cc.pusch.fhMode.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the frequency hopping mode in the PUSCH structure. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: hopping_mode: NONE No hopping INTer Inter subframe hopping INTRa Intra subframe hopping"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PUSCh:FHMode?')
		return Conversions.str_to_scalar_enum(response, enums.FreqHoppingMode)
