from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Npar:
	"""Npar commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("npar", core, parent)

	def set(self, value: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PUCCh:NPAR \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.pucch.npar.set(value = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the N_PUCCH parameter in the PUCCH structure settings. \n
			:param value: numeric value numeric value AUTO Determines the N_PUCCH based on the measurement. SUBF Selects the definition of N_PUCCH on subframe level.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(value)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PUCCh:NPAR {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PUCCh:NPAR \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.uplink.cc.pucch.npar.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the N_PUCCH parameter in the PUCCH structure settings. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: value: numeric value numeric value AUTO Determines the N_PUCCH based on the measurement. SUBF Selects the definition of N_PUCCH on subframe level."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PUCCh:NPAR?')
		return Conversions.str_to_float(response)
