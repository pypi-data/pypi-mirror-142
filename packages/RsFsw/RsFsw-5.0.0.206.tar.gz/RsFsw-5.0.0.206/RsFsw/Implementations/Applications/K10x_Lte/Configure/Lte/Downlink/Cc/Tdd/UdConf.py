from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UdConf:
	"""UdConf commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("udConf", core, parent)

	def set(self, configuration: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:TDD:UDConf \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.tdd.udConf.set(configuration = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the subframe configuration for TDD signals. \n
			:param configuration: numeric value (integer only) Range: 0 to 6
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(configuration)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:TDD:UDConf {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:TDD:UDConf \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.downlink.cc.tdd.udConf.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the subframe configuration for TDD signals. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: configuration: numeric value (integer only) Range: 0 to 6"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:TDD:UDConf?')
		return Conversions.str_to_float(response)
