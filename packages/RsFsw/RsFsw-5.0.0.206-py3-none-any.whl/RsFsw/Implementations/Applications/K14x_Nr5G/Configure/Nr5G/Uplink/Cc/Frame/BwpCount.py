from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BwpCount:
	"""BwpCount commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bwpCount", core, parent)

	def get(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default) -> float:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:FRAMe<fr>:BWPCount \n
		Snippet: value: float = driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.frame.bwpCount.get(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default) \n
		This command queries the number of analyzed bandwidth parts. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:return: bwps: numeric value (integer)"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		response = self._core.io.query_str(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPCount?')
		return Conversions.str_to_float(response)
