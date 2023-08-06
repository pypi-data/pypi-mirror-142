from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spsc:
	"""Spsc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spsc", core, parent)

	def set(self, configuration: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:TDD:SPSC \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.tdd.spsc.set(configuration = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the special TDD subframe configuration. \n
			:param configuration: numeric value (integer only) Numeric value that defines the subframe configuration. Subframe configurations 7 and 8 are only available if the cyclic prefix is normal. Range: 0 to 8
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(configuration)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:TDD:SPSC {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:TDD:SPSC \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.downlink.cc.tdd.spsc.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the special TDD subframe configuration. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: configuration: numeric value (integer only) Numeric value that defines the subframe configuration. Subframe configurations 7 and 8 are only available if the cyclic prefix is normal. Range: 0 to 8"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:TDD:SPSC?')
		return Conversions.str_to_float(response)
