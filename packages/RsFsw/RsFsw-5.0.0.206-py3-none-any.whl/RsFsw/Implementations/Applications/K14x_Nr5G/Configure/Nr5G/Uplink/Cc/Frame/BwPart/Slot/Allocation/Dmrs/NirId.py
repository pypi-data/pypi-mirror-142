from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup
from .............Internal import Conversions
from ............. import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NirId:
	"""NirId commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("nirId", core, parent)

	def set(self, value: float, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, slot=repcap.Slot.Default, allocation=repcap.Allocation.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:SLOT<sl>:ALLocation<al>:DMRS:NIRid \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.frame.bwPart.slot.allocation.dmrs.nirId.set(value = 1.0, carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default, slot = repcap.Slot.Default, allocation = repcap.Allocation.Default) \n
		This command defines the seed value for the PUSCH DM-RS sequence generation (transform precoding = on) .
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on transform precoding (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Tprecoding.set) .
			- Select sequence generation method n_ID^PUSCH (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Frame.BwPart.Slot.Allocation.Dmrs.Nirs.set) . \n
			:param value: numeric value (integer only)
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param slot: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param allocation: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Allocation')
		"""
		param = Conversions.decimal_value_to_str(value)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		self._core.io.write(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:SLOT{slot_cmd_val}:ALLocation{allocation_cmd_val}:DMRS:NIRid {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, slot=repcap.Slot.Default, allocation=repcap.Allocation.Default) -> float:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:SLOT<sl>:ALLocation<al>:DMRS:NIRid \n
		Snippet: value: float = driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.frame.bwPart.slot.allocation.dmrs.nirId.get(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default, slot = repcap.Slot.Default, allocation = repcap.Allocation.Default) \n
		This command defines the seed value for the PUSCH DM-RS sequence generation (transform precoding = on) .
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on transform precoding (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Tprecoding.set) .
			- Select sequence generation method n_ID^PUSCH (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Uplink.Cc.Frame.BwPart.Slot.Allocation.Dmrs.Nirs.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param slot: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param allocation: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Allocation')
			:return: value: numeric value (integer only)"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		response = self._core.io.query_str(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:SLOT{slot_cmd_val}:ALLocation{allocation_cmd_val}:DMRS:NIRid?')
		return Conversions.str_to_float(response)
