from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Idc:
	"""Idc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("idc", core, parent)

	def set(self, state: bool, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:IDC \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.idc.set(state = False, carrierComponent = repcap.CarrierComponent.Default) \n
		This command turns analysis of the DC carrier on and off. \n
			:param state: OFF | 0 Includes the DC carrier in the analysis. ON | 1 Excludes the DC carrier from the analysis. COMPensate Compensates the DC carrier.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.bool_to_str(state)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:IDC {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> bool:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:IDC \n
		Snippet: value: bool = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.idc.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command turns analysis of the DC carrier on and off. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: state: OFF | 0 Includes the DC carrier in the analysis. ON | 1 Excludes the DC carrier from the analysis. COMPensate Compensates the DC carrier."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:IDC?')
		return Conversions.str_to_bool(response)
