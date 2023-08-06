from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class N2Rb:
	"""N2Rb commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("n2Rb", core, parent)

	def set(self, value: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PUCCh:N2RB \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.pucch.n2Rb.set(value = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the N(2) _RB of the PUCCH. \n
			:param value: numeric value (integer only)
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(value)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PUCCh:N2RB {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PUCCh:N2RB \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.uplink.cc.pucch.n2Rb.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the N(2) _RB of the PUCCH. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: value: numeric value (integer only)"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PUCCh:N2RB?')
		return Conversions.str_to_float(response)
