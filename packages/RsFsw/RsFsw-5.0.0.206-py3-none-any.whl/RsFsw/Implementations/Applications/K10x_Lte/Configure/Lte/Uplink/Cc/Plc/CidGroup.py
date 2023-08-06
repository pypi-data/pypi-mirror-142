from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CidGroup:
	"""CidGroup commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cidGroup", core, parent)

	def set(self, group_number: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PLC:CIDGroup \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.plc.cidGroup.set(group_number = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the cell identity group. \n
			:param group_number: numeric value (integer only) Range: 1 to 167
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(group_number)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PLC:CIDGroup {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PLC:CIDGroup \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.uplink.cc.plc.cidGroup.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the cell identity group. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: group_number: numeric value (integer only) Range: 1 to 167"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PLC:CIDGroup?')
		return Conversions.str_to_float(response)
