from ............Internal.Core import Core
from ............Internal.CommandsGroup import CommandsGroup
from ............Internal import Conversions
from ............ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class VtpInter:
	"""VtpInter commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("vtpInter", core, parent)

	def set(self, type_py: float, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, slot=repcap.Slot.Default, allocation=repcap.Allocation.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:SLOT<sl>:ALLocation<al>:VTPinter \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.frame.bwPart.slot.allocation.vtpInter.set(type_py = 1.0, carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default, slot = repcap.Slot.Default, allocation = repcap.Allocation.Default) \n
		This command selects the interleaving size of VRB bundles. \n
			:param type_py: NINT No resource block bundling. numeric_value (integer only) Size of a VRB bundle (2 or 4 resource blocks) .
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param slot: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param allocation: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Allocation')
		"""
		param = Conversions.decimal_value_to_str(type_py)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:SLOT{slot_cmd_val}:ALLocation{allocation_cmd_val}:VTPinter {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default, frame=repcap.Frame.Default, bwPart=repcap.BwPart.Default, slot=repcap.Slot.Default, allocation=repcap.Allocation.Default) -> float:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FRAMe<fr>:BWPart<bwp>:SLOT<sl>:ALLocation<al>:VTPinter \n
		Snippet: value: float = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.frame.bwPart.slot.allocation.vtpInter.get(carrierComponent = repcap.CarrierComponent.Default, frame = repcap.Frame.Default, bwPart = repcap.BwPart.Default, slot = repcap.Slot.Default, allocation = repcap.Allocation.Default) \n
		This command selects the interleaving size of VRB bundles. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param frame: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Frame')
			:param bwPart: optional repeated capability selector. Default value: Nr1 (settable in the interface 'BwPart')
			:param slot: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Slot')
			:param allocation: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Allocation')
			:return: type_py: NINT No resource block bundling. numeric_value (integer only) Size of a VRB bundle (2 or 4 resource blocks) ."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		frame_cmd_val = self._cmd_group.get_repcap_cmd_value(frame, repcap.Frame)
		bwPart_cmd_val = self._cmd_group.get_repcap_cmd_value(bwPart, repcap.BwPart)
		slot_cmd_val = self._cmd_group.get_repcap_cmd_value(slot, repcap.Slot)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FRAMe{frame_cmd_val}:BWPart{bwPart_cmd_val}:SLOT{slot_cmd_val}:ALLocation{allocation_cmd_val}:VTPinter?')
		return Conversions.str_to_float(response)
