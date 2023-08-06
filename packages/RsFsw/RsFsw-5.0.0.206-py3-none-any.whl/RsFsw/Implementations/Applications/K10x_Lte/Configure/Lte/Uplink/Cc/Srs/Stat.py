from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stat:
	"""Stat commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stat", core, parent)

	def set(self, state: bool, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:SRS:STAT \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.srs.stat.set(state = False, carrierComponent = repcap.CarrierComponent.Default) \n
		Turns the sounding reference signal on and off. \n
			:param state: ON | OFF | 1 | 0
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.bool_to_str(state)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:SRS:STAT {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> bool:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:SRS:STAT \n
		Snippet: value: bool = driver.applications.k10Xlte.configure.lte.uplink.cc.srs.stat.get(carrierComponent = repcap.CarrierComponent.Default) \n
		Turns the sounding reference signal on and off. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: state: ON | OFF | 1 | 0"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:SRS:STAT?')
		return Conversions.str_to_bool(response)
