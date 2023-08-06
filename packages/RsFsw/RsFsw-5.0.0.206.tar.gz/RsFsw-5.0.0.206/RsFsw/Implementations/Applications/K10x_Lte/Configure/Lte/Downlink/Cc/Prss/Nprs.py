from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Nprs:
	"""Nprs commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nprs", core, parent)

	def set(self, no_of_subframes: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:PRSS:NPRS \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.prss.nprs.set(no_of_subframes = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the number of subframes the positioning reference signal occupies. \n
			:param no_of_subframes: No help available
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(no_of_subframes)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:PRSS:NPRS {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:PRSS:NPRS \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.downlink.cc.prss.nprs.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the number of subframes the positioning reference signal occupies. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: no_of_subframes: No help available"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:PRSS:NPRS?')
		return Conversions.str_to_float(response)
