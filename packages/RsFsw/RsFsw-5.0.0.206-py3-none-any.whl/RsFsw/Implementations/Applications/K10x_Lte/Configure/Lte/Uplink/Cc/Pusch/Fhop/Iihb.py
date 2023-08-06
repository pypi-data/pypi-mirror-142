from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iihb:
	"""Iihb commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iihb", core, parent)

	def set(self, hb_info: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PUSCh:FHOP:IIHB \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.pusch.fhop.iihb.set(hb_info = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the information in hopping bits of the PUSCH. \n
			:param hb_info: numeric value Range: 0 to 3
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(hb_info)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PUSCh:FHOP:IIHB {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PUSCh:FHOP:IIHB \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.uplink.cc.pusch.fhop.iihb.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the information in hopping bits of the PUSCH. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: hb_info: numeric value Range: 0 to 3"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PUSCh:FHOP:IIHB?')
		return Conversions.str_to_float(response)
