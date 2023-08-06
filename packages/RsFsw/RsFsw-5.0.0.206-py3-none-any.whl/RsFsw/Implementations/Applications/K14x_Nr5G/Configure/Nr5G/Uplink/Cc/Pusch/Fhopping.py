from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fhopping:
	"""Fhopping commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fhopping", core, parent)

	def set(self, mode: enums.FreqhopingMode, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:PUSCh:FHOPping \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.pusch.fhopping.set(mode = enums.FreqhopingMode.DISable, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the PUSCH frequency hopping mode.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Configure exactly one PUSCH allocation. \n
			:param mode: DISable No PUSCH frequency hopping. INTRa Intra-slot frequency hopping.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.FreqhopingMode)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:PUSCh:FHOPping {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.FreqhopingMode:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:PUSCh:FHOPping \n
		Snippet: value: enums.FreqhopingMode = driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.pusch.fhopping.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the PUSCH frequency hopping mode.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Configure exactly one PUSCH allocation. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: mode: DISable No PUSCH frequency hopping. INTRa Intra-slot frequency hopping."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:PUSCh:FHOPping?')
		return Conversions.str_to_scalar_enum(response, enums.FreqhopingMode)
