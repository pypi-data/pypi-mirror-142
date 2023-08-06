from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sindex:
	"""Sindex commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sindex", core, parent)

	def set(self, index: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PRACh:SINDex \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.prach.sindex.set(index = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the PRACH sequence index. \n
			:param index: IndexValue Number that defines the index manually. AUTO Automatically determines the index.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(index)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PRACh:SINDex {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PRACh:SINDex \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.uplink.cc.prach.sindex.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the PRACH sequence index. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: index: IndexValue Number that defines the index manually. AUTO Automatically determines the index."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PRACh:SINDex?')
		return Conversions.str_to_float(response)
