from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sspacing:
	"""Sspacing commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sspacing", core, parent)

	def set(self, subcarrier_spacing: enums.SubcarrierSpacing, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:SSPacing \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.frame.bwPart.sspacing.set(subcarrier_spacing = enums.SubcarrierSpacing.SS120, carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default) \n
		This command selects the subcarrier spacing of a bandwidth part. \n
			:param subcarrier_spacing: SS15 15 kHz subcarrier spacing. Only for signal deployment in FR1. SS30 30 kHz subcarrier spacing. Only for signal deployment in FR1. SS60 60 kHz subcarrier spacing with normal cyclic prefix. For all signal deployments. SS120 120 kHz subcarrier spacing. Only for signal deployment in FR2. X60 60 kHz subcarrier spacing with extended cyclic prefix. For all signal deployments.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
		"""
		param = Conversions.enum_scalar_to_str(subcarrier_spacing, enums.SubcarrierSpacing)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		self._core.io.write(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:SSPacing {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default) -> enums.SubcarrierSpacing:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:SSPacing \n
		Snippet: value: enums.SubcarrierSpacing = driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.frame.bwPart.sspacing.get(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default) \n
		This command selects the subcarrier spacing of a bandwidth part. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:return: subcarrier_spacing: SS15 15 kHz subcarrier spacing. Only for signal deployment in FR1. SS30 30 kHz subcarrier spacing. Only for signal deployment in FR1. SS60 60 kHz subcarrier spacing with normal cyclic prefix. For all signal deployments. SS120 120 kHz subcarrier spacing. Only for signal deployment in FR2. X60 60 kHz subcarrier spacing with extended cyclic prefix. For all signal deployments."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		response = self._core.io.query_str(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:SSPacing?')
		return Conversions.str_to_scalar_enum(response, enums.SubcarrierSpacing)
