from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FrIndex:
	"""FrIndex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frIndex", core, parent)

	def set(self, frequency_index: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PRACh:FRINdex \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.prach.frIndex.set(frequency_index = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the PRACH frequency index. \n
			:param frequency_index: numeric value (integer only)
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(frequency_index)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PRACh:FRINdex {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PRACh:FRINdex \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.uplink.cc.prach.frIndex.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the PRACH frequency index. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: frequency_index: numeric value (integer only)"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PRACh:FRINdex?')
		return Conversions.str_to_float(response)
