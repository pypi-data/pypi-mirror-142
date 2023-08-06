from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import enums
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Detection:
	"""Detection commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("detection", core, parent)

	def set(self, state: enums.AutoManualMode, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:DETection \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.frame.bwPart.detection.set(state = enums.AutoManualMode.AUTO, carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default) \n
		This command turns automatic signal demodulation on and off. \n
			:param state: AUTO Automatic signal detection = on. MANual Automatic signal detection = off.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
		"""
		param = Conversions.enum_scalar_to_str(state, enums.AutoManualMode)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		self._core.io.write(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:DETection {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default) -> enums.AutoManualMode:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:DETection \n
		Snippet: value: enums.AutoManualMode = driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.frame.bwPart.detection.get(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default) \n
		This command turns automatic signal demodulation on and off. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:return: state: AUTO Automatic signal detection = on. MANual Automatic signal detection = off."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		response = self._core.io.query_str(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:DETection?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)
