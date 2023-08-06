from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pb:
	"""Pb commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pb", core, parent)

	def set(self, power_ratio: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:PDSCh:PB \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.pdsch.pb.set(power_ratio = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the PDSCH power ratio. Note that the power ratio depends on the number of antennas in the system. \n
			:param power_ratio: Numeric value that defines PDSCH P_B which defines the power ratio in dB. 0 | 1 | 2 | 3 See 'PDSCH Power Ratio' for an overview of resulting power ratios. RAT1 Ratio = 1, regardless of the number of antennas.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(power_ratio)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:PDSCh:PB {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:PDSCh:PB \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.downlink.cc.pdsch.pb.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the PDSCH power ratio. Note that the power ratio depends on the number of antennas in the system. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: power_ratio: Numeric value that defines PDSCH P_B which defines the power ratio in dB. 0 | 1 | 2 | 3 See 'PDSCH Power Ratio' for an overview of resulting power ratios. RAT1 Ratio = 1, regardless of the number of antennas."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:PDSCh:PB?')
		return Conversions.str_to_float(response)
