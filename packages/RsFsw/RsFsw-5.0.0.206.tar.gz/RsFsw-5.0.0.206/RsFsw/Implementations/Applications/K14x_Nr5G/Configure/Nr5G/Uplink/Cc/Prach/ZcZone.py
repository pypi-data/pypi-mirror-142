from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ZcZone:
	"""ZcZone commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("zcZone", core, parent)

	def set(self, index: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:PRACh:ZCZone \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.prach.zcZone.set(index = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the PRACH zero correlation zone. \n
			:param index: Component Carrier
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(index)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:PRACh:ZCZone {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:PRACh:ZCZone \n
		Snippet: value: float = driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.prach.zcZone.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the PRACH zero correlation zone. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: index: No help available"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:PRACh:ZCZone?')
		return Conversions.str_to_float(response)
