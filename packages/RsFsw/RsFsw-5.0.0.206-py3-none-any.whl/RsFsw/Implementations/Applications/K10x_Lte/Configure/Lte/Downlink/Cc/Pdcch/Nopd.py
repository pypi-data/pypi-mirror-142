from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nopd:
	"""Nopd commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nopd", core, parent)

	def set(self, quantity: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:PDCCh:NOPD \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.pdcch.nopd.set(quantity = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command sets the number of PDCCHs. \n
			:param quantity: numeric value
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(quantity)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:PDCCh:NOPD {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:PDCCh:NOPD \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.downlink.cc.pdcch.nopd.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command sets the number of PDCCHs. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: quantity: numeric value"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:PDCCh:NOPD?')
		return Conversions.str_to_float(response)
