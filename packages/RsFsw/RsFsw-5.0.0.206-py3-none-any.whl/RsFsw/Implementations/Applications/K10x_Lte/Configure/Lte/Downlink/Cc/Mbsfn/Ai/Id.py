from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Id:
	"""Id commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("id", core, parent)

	def set(self, idn: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:MBSFn:AI:ID \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.mbsfn.ai.id.set(idn = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		Defines the ID of an MBFSN area. \n
			:param idn: Range: 0 to 255
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(idn)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:MBSFn:AI:ID {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:MBSFn:AI:ID \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.downlink.cc.mbsfn.ai.id.get(carrierComponent = repcap.CarrierComponent.Default) \n
		Defines the ID of an MBFSN area. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: idn: Range: 0 to 255"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:MBSFn:AI:ID?')
		return Conversions.str_to_float(response)
