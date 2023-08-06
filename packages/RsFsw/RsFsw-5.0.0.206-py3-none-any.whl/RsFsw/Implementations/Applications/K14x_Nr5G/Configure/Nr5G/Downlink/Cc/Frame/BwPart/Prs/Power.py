from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	def set(self, power: float, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:PRS:POWer \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.frame.bwPart.prs.power.set(power = 1.0, carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default) \n
		This command defines the relative power of the positioning reference signal. \n
			:param power: Unit: dB
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
		"""
		param = Conversions.decimal_value_to_str(power)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:PRS:POWer {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default) -> float:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:PRS:POWer \n
		Snippet: value: float = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.frame.bwPart.prs.power.get(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default) \n
		This command defines the relative power of the positioning reference signal. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:return: power: Unit: dB"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:PRS:POWer?')
		return Conversions.str_to_float(response)
