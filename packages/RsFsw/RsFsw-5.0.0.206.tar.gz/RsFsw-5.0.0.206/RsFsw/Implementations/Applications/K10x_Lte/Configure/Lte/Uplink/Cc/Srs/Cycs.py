from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cycs:
	"""Cycs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cycs", core, parent)

	def set(self, cyclic_shift: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:SRS:CYCS \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.srs.cycs.set(cyclic_shift = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		Sets the cyclic shift n_CS used for the generation of the sounding reference signal CAZAC sequence. \n
			:param cyclic_shift: numeric value
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(cyclic_shift)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:SRS:CYCS {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:SRS:CYCS \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.uplink.cc.srs.cycs.get(carrierComponent = repcap.CarrierComponent.Default) \n
		Sets the cyclic shift n_CS used for the generation of the sounding reference signal CAZAC sequence. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: cyclic_shift: numeric value"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:SRS:CYCS?')
		return Conversions.str_to_float(response)
