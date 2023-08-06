from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UeId:
	"""UeId commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ueId", core, parent)

	def set(self, idn: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:UEID \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.ueId.set(idn = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the radio network temporary identifier (RNTI) of the UE. \n
			:param idn: numeric value (integer only) Range: 0 to 65535
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(idn)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:UEID {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:UEID \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.uplink.cc.ueId.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the radio network temporary identifier (RNTI) of the UE. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: idn: numeric value (integer only) Range: 0 to 65535"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:UEID?')
		return Conversions.str_to_float(response)
