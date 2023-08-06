from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nosm:
	"""Nosm commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nosm", core, parent)

	def set(self, no_of_subbands: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PUSCh:NOSM \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.pusch.nosm.set(no_of_subbands = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the number of subbands/M of the PUSCH. \n
			:param no_of_subbands: numeric value
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(no_of_subbands)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PUSCh:NOSM {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PUSCh:NOSM \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.uplink.cc.pusch.nosm.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the number of subbands/M of the PUSCH. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: no_of_subbands: numeric value"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PUSCh:NOSM?')
		return Conversions.str_to_float(response)
