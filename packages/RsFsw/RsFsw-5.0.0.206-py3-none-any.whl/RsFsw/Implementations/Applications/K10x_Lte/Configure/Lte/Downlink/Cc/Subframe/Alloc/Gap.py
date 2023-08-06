from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gap:
	"""Gap commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gap", core, parent)

	def set(self, vrb_gap: float, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default, allocation=repcap.Allocation.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:SUBFrame<sf>:ALLoc<al>:GAP \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.subframe.alloc.gap.set(vrb_gap = 1.0, carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default, allocation = repcap.Allocation.Default) \n
		This command turns the VRB Gap on and off. \n
			:param vrb_gap: 0 Selects localized VRBs 1 Selects distributed VRBs and applies the first gap 2 Selects distributed VRBs and applies the second gap (for channel bandwidths 50 resource blocks)
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
			:param allocation: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.decimal_value_to_str(vrb_gap)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:SUBFrame{subframe_cmd_val}:ALLoc{allocation_cmd_val}:GAP {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default, allocation=repcap.Allocation.Default) -> float:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:SUBFrame<sf>:ALLoc<al>:GAP \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.downlink.cc.subframe.alloc.gap.get(carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default, allocation = repcap.Allocation.Default) \n
		This command turns the VRB Gap on and off. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
			:param allocation: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: vrb_gap: 0 Selects localized VRBs 1 Selects distributed VRBs and applies the first gap 2 Selects distributed VRBs and applies the second gap (for channel bandwidths 50 resource blocks)"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:SUBFrame{subframe_cmd_val}:ALLoc{allocation_cmd_val}:GAP?')
		return Conversions.str_to_float(response)
