from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Plid:
	"""Plid commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plid", core, parent)

	def set(self, identity: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PUCCh:PLID \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.pucch.plid.set(identity = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the (cell) identity of the PUCCH. \n
			:param identity: FCID From cell ID: Uses the common Identity defined with method RsFsw.Applications.K10x_Lte.Configure.Lte.Uplink.Cc.Plc.Plid.set. numeric value Custom identity for the PUCCH (range: 1...2) .
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(identity)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PUCCh:PLID {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PUCCh:PLID \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.uplink.cc.pucch.plid.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the (cell) identity of the PUCCH. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: identity: FCID From cell ID: Uses the common Identity defined with method RsFsw.Applications.K10x_Lte.Configure.Lte.Uplink.Cc.Plc.Plid.set. numeric value Custom identity for the PUCCH (range: 1...2) ."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PUCCh:PLID?')
		return Conversions.str_to_float(response)
