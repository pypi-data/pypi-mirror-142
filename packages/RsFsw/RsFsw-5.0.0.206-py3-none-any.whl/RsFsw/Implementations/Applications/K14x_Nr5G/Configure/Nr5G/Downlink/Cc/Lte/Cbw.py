from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cbw:
	"""Cbw commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cbw", core, parent)

	def set(self, resource_blocks: enums.LteCarrResourceBlocks, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:LTE:CBW \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.lte.cbw.set(resource_blocks = enums.LteCarrResourceBlocks.N100, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the channel bandwidth of an LTE carrier.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on LTE-CRS coexistence (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Lte.State.set) . \n
			:param resource_blocks: N6 | N15 | N25 | N50 | N75 | N100
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(resource_blocks, enums.LteCarrResourceBlocks)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:LTE:CBW {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.LteCarrResourceBlocks:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:LTE:CBW \n
		Snippet: value: enums.LteCarrResourceBlocks = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.lte.cbw.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the channel bandwidth of an LTE carrier.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on LTE-CRS coexistence (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Lte.State.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: resource_blocks: N6 | N15 | N25 | N50 | N75 | N100"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:LTE:CBW?')
		return Conversions.str_to_scalar_enum(response, enums.LteCarrResourceBlocks)
