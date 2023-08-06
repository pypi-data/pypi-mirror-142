from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup
from .............Internal import Conversions
from ............. import enums
from ............. import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.PasteLogicMode, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, slot=repcap.Slot.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:SLOT<sl>:PASTe:TO:MODE \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.frame.bwPart.slot.paste.to.mode.set(mode = enums.PasteLogicMode.CUSTom, carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default, slot = repcap.Slot.Default) \n
		This command selects the paste logic when you copy a slot configuration to other slots.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- A slot configuration is in the clipboard (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Frame.BwPart.Slot.copy) .
			- Number of configurable slots > 1 (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Frame.BwPart.Cslot.set) . \n
			:param mode: CUSTom Copies the slot configuration to specific set of slots according to the logic defined with: •method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Frame.BwPart.Slot.Paste.To.Period.set •method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Frame.BwPart.Slot.Paste.To.Duration.set DATA Copies the slot configuration to all data slots. SLOTs Copies the slot configuration to a specific set of slots. UNUSed Copies the slot configuration to all unused slots.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param slot: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.PasteLogicMode)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		self._core.io.write(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:SLOT{slot_cmd_val}:PASTe:TO:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, slot=repcap.Slot.Default) -> enums.PasteLogicMode:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:SLOT<sl>:PASTe:TO:MODE \n
		Snippet: value: enums.PasteLogicMode = driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.frame.bwPart.slot.paste.to.mode.get(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default, slot = repcap.Slot.Default) \n
		This command selects the paste logic when you copy a slot configuration to other slots.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- A slot configuration is in the clipboard (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Frame.BwPart.Slot.copy) .
			- Number of configurable slots > 1 (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Frame.BwPart.Cslot.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param slot: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:return: mode: CUSTom Copies the slot configuration to specific set of slots according to the logic defined with: •method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Frame.BwPart.Slot.Paste.To.Period.set •method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Frame.BwPart.Slot.Paste.To.Duration.set DATA Copies the slot configuration to all data slots. SLOTs Copies the slot configuration to a specific set of slots. UNUSed Copies the slot configuration to all unused slots."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		response = self._core.io.query_str(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:SLOT{slot_cmd_val}:PASTe:TO:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.PasteLogicMode)
