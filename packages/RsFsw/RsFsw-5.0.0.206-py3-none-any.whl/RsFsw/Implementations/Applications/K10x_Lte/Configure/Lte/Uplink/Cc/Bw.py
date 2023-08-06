from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bw:
	"""Bw commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bw", core, parent)

	def set(self, bandwidth: enums.BandwidthLteB, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:BW \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.bw.set(bandwidth = enums.BandwidthLteB.BW1_40, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the channel bandwidth. \n
			:param bandwidth: BW1_40 | BW3_00 | BW5_00 | BW10_00 | BW15_00 | BW20_00
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(bandwidth, enums.BandwidthLteB)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:BW {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.BandwidthLteB:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:BW \n
		Snippet: value: enums.BandwidthLteB = driver.applications.k10Xlte.configure.lte.uplink.cc.bw.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the channel bandwidth. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: bandwidth: BW1_40 | BW3_00 | BW5_00 | BW10_00 | BW15_00 | BW20_00"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:BW?')
		return Conversions.str_to_scalar_enum(response, enums.BandwidthLteB)
