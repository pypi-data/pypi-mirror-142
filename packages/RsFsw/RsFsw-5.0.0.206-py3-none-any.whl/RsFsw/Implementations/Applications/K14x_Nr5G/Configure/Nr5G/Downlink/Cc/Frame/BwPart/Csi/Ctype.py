from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ctype:
	"""Ctype commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ctype", core, parent)

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, csiRs=repcap.CsiRs.Default) -> enums.CdmType:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:CSI<csi>:CTYPe \n
		Snippet: value: enums.CdmType = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.frame.bwPart.csi.ctype.get(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default, csiRs = repcap.CsiRs.Default) \n
		This command queries the CDM type of the CSI-RS. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param csiRs: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Csi')
			:return: cdm_type: NOCDm | FDCDm2 | CDM4 | CDM8"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		csiRs_cmd_val = self._cmd_group.get_repcap_cmd_value(csiRs, repcap.CsiRs)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:CSI{csiRs_cmd_val}:CTYPe?')
		return Conversions.str_to_scalar_enum(response, enums.CdmType)
