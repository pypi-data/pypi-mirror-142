from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nprb:
	"""Nprb commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nprb", core, parent)

	def set(self, resource_blocks: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:EPDCch:NPRB \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.epdcch.nprb.set(resource_blocks = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the number of resource blocks that the EPDCCH-PRB set uses. \n
			:param resource_blocks: 0 | 2 | 4 | 8 When you select '0', the EPDCCH i not active.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(resource_blocks)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:EPDCch:NPRB {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:EPDCch:NPRB \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.downlink.cc.epdcch.nprb.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the number of resource blocks that the EPDCCH-PRB set uses. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: resource_blocks: 0 | 2 | 4 | 8 When you select '0', the EPDCCH i not active."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:EPDCch:NPRB?')
		return Conversions.str_to_float(response)
