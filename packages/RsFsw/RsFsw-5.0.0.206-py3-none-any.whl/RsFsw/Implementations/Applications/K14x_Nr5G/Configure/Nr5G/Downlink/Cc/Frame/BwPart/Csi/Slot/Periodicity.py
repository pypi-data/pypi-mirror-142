from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import enums
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Periodicity:
	"""Periodicity commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("periodicity", core, parent)

	def set(self, slot: enums.Slot, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, csiRs=repcap.CsiRs.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:CSI<csi>:SLOT:PERiodicity \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.frame.bwPart.csi.slot.periodicity.set(slot = enums.Slot.S160, carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default, csiRs = repcap.CsiRs.Default) \n
		This command selects the periodicity of CSI-RS transmission in terms of slots.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select periodic transmission (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Frame.BwPart.Csi.Slot.Mode.set) . \n
			:param slot: SL4 | SL5 | SL8 | SL10 | SL16 | SL20 | SL32 | SL40 | SL64 | SL80 | S160 | S320 | S640 Example: SL4 selects a periodicity of 4 (transmission every four slots) . The availability of parameters depends on the subcarrier spacing in the bandwidth part you are configuring.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param csiRs: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Csi')
		"""
		param = Conversions.enum_scalar_to_str(slot, enums.Slot)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		csiRs_cmd_val = self._cmd_group.get_repcap_cmd_value(csiRs, repcap.CsiRs)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:CSI{csiRs_cmd_val}:SLOT:PERiodicity {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, csiRs=repcap.CsiRs.Default) -> enums.Slot:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:CSI<csi>:SLOT:PERiodicity \n
		Snippet: value: enums.Slot = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.frame.bwPart.csi.slot.periodicity.get(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default, csiRs = repcap.CsiRs.Default) \n
		This command selects the periodicity of CSI-RS transmission in terms of slots.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select periodic transmission (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Frame.BwPart.Csi.Slot.Mode.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param csiRs: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Csi')
			:return: slot: SL4 | SL5 | SL8 | SL10 | SL16 | SL20 | SL32 | SL40 | SL64 | SL80 | S160 | S320 | S640 Example: SL4 selects a periodicity of 4 (transmission every four slots) . The availability of parameters depends on the subcarrier spacing in the bandwidth part you are configuring."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		csiRs_cmd_val = self._cmd_group.get_repcap_cmd_value(csiRs, repcap.CsiRs)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:CSI{csiRs_cmd_val}:SLOT:PERiodicity?')
		return Conversions.str_to_scalar_enum(response, enums.Slot)
