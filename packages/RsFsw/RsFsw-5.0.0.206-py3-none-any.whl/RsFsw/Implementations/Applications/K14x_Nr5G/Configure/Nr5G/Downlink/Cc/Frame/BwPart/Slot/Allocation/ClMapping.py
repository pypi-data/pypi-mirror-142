from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import enums
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ClMapping:
	"""ClMapping commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("clMapping", core, parent)

	def set(self, mapping: enums.AllocMapping, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, slot=repcap.Slot.Default, allocation=repcap.Allocation.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:SLOT<sl>:ALLocation<al>:CLMapping \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.frame.bwPart.slot.allocation.clMapping.set(mapping = enums.AllocMapping.LC101, carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default, slot = repcap.Slot.Default, allocation = repcap.Allocation.Default) \n
		This command selects the codeword to layer mapping. \n
			:param mapping: LC11 | LC21 | LC31 | LC41 | LC51 | LC61 | LC71 | LC81 | LC91 | LC101 | LC111 | LC121 | LC22 | LC32 | LC42 | LC52 | LC62 | LC72 | LC82 The availability of codeword to layer mappings depends on: • DM-RS configuration type (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Frame.BwPart.Slot.Allocation.Dmrs.Ctype.set) • DM-RS length (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Frame.BwPart.Slot.Allocation.Dmrs.Msymbol.Length.set)
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param slot: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param allocation: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Allocation')
		"""
		param = Conversions.enum_scalar_to_str(mapping, enums.AllocMapping)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:SLOT{slot_cmd_val}:ALLocation{allocation_cmd_val}:CLMapping {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, slot=repcap.Slot.Default, allocation=repcap.Allocation.Default) -> enums.AllocMapping:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:SLOT<sl>:ALLocation<al>:CLMapping \n
		Snippet: value: enums.AllocMapping = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.frame.bwPart.slot.allocation.clMapping.get(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default, slot = repcap.Slot.Default, allocation = repcap.Allocation.Default) \n
		This command selects the codeword to layer mapping. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param slot: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param allocation: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Allocation')
			:return: mapping: LC11 | LC21 | LC31 | LC41 | LC51 | LC61 | LC71 | LC81 | LC91 | LC101 | LC111 | LC121 | LC22 | LC32 | LC42 | LC52 | LC62 | LC72 | LC82 The availability of codeword to layer mappings depends on: • DM-RS configuration type (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Frame.BwPart.Slot.Allocation.Dmrs.Ctype.set) • DM-RS length (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Frame.BwPart.Slot.Allocation.Dmrs.Msymbol.Length.set)"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:SLOT{slot_cmd_val}:ALLocation{allocation_cmd_val}:CLMapping?')
		return Conversions.str_to_scalar_enum(response, enums.AllocMapping)
