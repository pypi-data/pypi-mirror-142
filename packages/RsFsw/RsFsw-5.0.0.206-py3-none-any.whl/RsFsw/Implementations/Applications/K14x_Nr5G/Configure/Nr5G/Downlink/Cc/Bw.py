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

	def set(self, bandwidth: enums.BandwidthNr5G, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:BW \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.bw.set(bandwidth = enums.BandwidthNr5G.BW10, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the channel bandwidth of the 5G NR carrier. \n
			:param bandwidth: BW5 | BW10 | BW15 | BW20 | BW25 | BW30 | BW40 | BW50 | BW60 | BW70 | BW80 | BW90 | BW100 | BW200 | BW400
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(bandwidth, enums.BandwidthNr5G)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:BW {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.BandwidthNr5G:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:BW \n
		Snippet: value: enums.BandwidthNr5G = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.bw.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the channel bandwidth of the 5G NR carrier. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: bandwidth: BW5 | BW10 | BW15 | BW20 | BW25 | BW30 | BW40 | BW50 | BW60 | BW70 | BW80 | BW90 | BW100 | BW200 | BW400"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:BW?')
		return Conversions.str_to_scalar_enum(response, enums.BandwidthNr5G)
