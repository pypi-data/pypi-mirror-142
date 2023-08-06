from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Anst:
	"""Anst commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("anst", core, parent)

	def set(self, state: bool, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:SRS:ANST \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.srs.anst.set(state = False, carrierComponent = repcap.CarrierComponent.Default) \n
		This command turns simultaneous transmission of the sounding reference signal (SRS) and ACK/NACK messages (via PUCCH) on
		and off. Simultaneous transmission works only if the PUCCH format ist either 1, 1a, 1b or 3. \n
			:param state: ON Allows simultaneous transmission of SRS and PUCCH. OFF SRS not transmitted in the subframe for which you have configured simultaneous transmission of PUCCH and SRS.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.bool_to_str(state)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:SRS:ANST {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> bool:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:SRS:ANST \n
		Snippet: value: bool = driver.applications.k10Xlte.configure.lte.uplink.cc.srs.anst.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command turns simultaneous transmission of the sounding reference signal (SRS) and ACK/NACK messages (via PUCCH) on
		and off. Simultaneous transmission works only if the PUCCH format ist either 1, 1a, 1b or 3. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: state: ON Allows simultaneous transmission of SRS and PUCCH. OFF SRS not transmitted in the subframe for which you have configured simultaneous transmission of PUCCH and SRS."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:SRS:ANST?')
		return Conversions.str_to_bool(response)
