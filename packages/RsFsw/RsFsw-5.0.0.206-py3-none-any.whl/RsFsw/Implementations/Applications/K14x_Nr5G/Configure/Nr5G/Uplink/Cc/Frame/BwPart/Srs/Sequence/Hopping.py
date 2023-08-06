from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import enums
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hopping:
	"""Hopping commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hopping", core, parent)

	def set(self, hopping: enums.HoppingMode, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:SRS:SEQuence:HOPPing \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.frame.bwPart.srs.sequence.hopping.set(hopping = enums.HoppingMode.GROup, carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default) \n
		This command select the frequency hopping method for the sounding reference signal.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on SRS (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Frame.BwPart.Srs.State.set) . \n
			:param hopping: GROup Group hopping. SEQuence Sequence hopping. NONE No hopping.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
		"""
		param = Conversions.enum_scalar_to_str(hopping, enums.HoppingMode)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		self._core.io.write(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:SRS:SEQuence:HOPPing {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default) -> enums.HoppingMode:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:SRS:SEQuence:HOPPing \n
		Snippet: value: enums.HoppingMode = driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.frame.bwPart.srs.sequence.hopping.get(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default) \n
		This command select the frequency hopping method for the sounding reference signal.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on SRS (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Frame.BwPart.Srs.State.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:return: hopping: GROup Group hopping. SEQuence Sequence hopping. NONE No hopping."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		response = self._core.io.query_str(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:SRS:SEQuence:HOPPing?')
		return Conversions.str_to_scalar_enum(response, enums.HoppingMode)
