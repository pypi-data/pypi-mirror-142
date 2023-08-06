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

	def set(self, mode: enums.CopyLogicMode, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, slot=repcap.Slot.Default, allocation=repcap.Allocation.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:SLOT<sl>:ALLocation<al>:COPY:MODE \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.frame.bwPart.slot.allocation.copy.mode.set(mode = enums.CopyLogicMode.CUSTom, carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default, slot = repcap.Slot.Default, allocation = repcap.Allocation.Default) \n
		This command selects the paste logic when you copy a PUSCH configuration to other slots.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Number of configurable slots > 1 (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Frame.BwPart.Cslot.set) . \n
			:param mode: CUSTom Copies the slot configuration to specific set of slots according to the logic defined with: •method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Frame.BwPart.Slot.Allocation.Copy.Period.set •method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Frame.BwPart.Slot.Allocation.Copy.Duration.set SLOT Copies the slot configuration to a specific set of slots. Select the slots with method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Frame.BwPart.Slot.Allocation.Copy.Slot.set.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param slot: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param allocation: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Allocation')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.CopyLogicMode)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		self._core.io.write(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:SLOT{slot_cmd_val}:ALLocation{allocation_cmd_val}:COPY:MODE {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, slot=repcap.Slot.Default, allocation=repcap.Allocation.Default) -> enums.CopyLogicMode:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:SLOT<sl>:ALLocation<al>:COPY:MODE \n
		Snippet: value: enums.CopyLogicMode = driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.frame.bwPart.slot.allocation.copy.mode.get(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default, slot = repcap.Slot.Default, allocation = repcap.Allocation.Default) \n
		This command selects the paste logic when you copy a PUSCH configuration to other slots.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Number of configurable slots > 1 (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Frame.BwPart.Cslot.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param slot: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param allocation: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Allocation')
			:return: mode: CUSTom Copies the slot configuration to specific set of slots according to the logic defined with: •method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Frame.BwPart.Slot.Allocation.Copy.Period.set •method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Frame.BwPart.Slot.Allocation.Copy.Duration.set SLOT Copies the slot configuration to a specific set of slots. Select the slots with method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Frame.BwPart.Slot.Allocation.Copy.Slot.set."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		response = self._core.io.query_str(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:SLOT{slot_cmd_val}:ALLocation{allocation_cmd_val}:COPY:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.CopyLogicMode)
