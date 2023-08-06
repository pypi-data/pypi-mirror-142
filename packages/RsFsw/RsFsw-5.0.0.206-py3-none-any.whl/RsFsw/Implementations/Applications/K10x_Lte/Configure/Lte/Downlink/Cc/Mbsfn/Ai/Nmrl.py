from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nmrl:
	"""Nmrl commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nmrl", core, parent)

	def set(self, configuration: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:MBSFn:AI:NMRL \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.mbsfn.ai.nmrl.set(configuration = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the length of the control data region in an MBSFN subframe. \n
			:param configuration: 1 The first symbol in a subframe carries data of the control channel. 2 The first two symbols in a subframe carry data of the control channel.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(configuration)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:MBSFn:AI:NMRL {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:MBSFn:AI:NMRL \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.downlink.cc.mbsfn.ai.nmrl.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the length of the control data region in an MBSFN subframe. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: configuration: 1 The first symbol in a subframe carries data of the control channel. 2 The first two symbols in a subframe carry data of the control channel."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:MBSFn:AI:NMRL?')
		return Conversions.str_to_float(response)
