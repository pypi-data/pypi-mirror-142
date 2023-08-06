from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup
from ..........Internal import Conversions
from .......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RbCount:
	"""RbCount commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rbCount", core, parent)

	def set(self, resource_blocks: float, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default, allocation=repcap.Allocation.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:SUBFrame<sf>:ALLoc<al>:RBCount \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.subframe.alloc.rbCount.set(resource_blocks = 1.0, carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default, allocation = repcap.Allocation.Default) \n
		This command selects the number of resource blocks of an allocation in a downlink subframe. \n
			:param resource_blocks: numeric value
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
			:param allocation: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
		"""
		param = Conversions.decimal_value_to_str(resource_blocks)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:SUBFrame{subframe_cmd_val}:ALLoc{allocation_cmd_val}:RBCount {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default, allocation=repcap.Allocation.Default) -> float:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:SUBFrame<sf>:ALLoc<al>:RBCount \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.downlink.cc.subframe.alloc.rbCount.get(carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default, allocation = repcap.Allocation.Default) \n
		This command selects the number of resource blocks of an allocation in a downlink subframe. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
			:param allocation: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Alloc')
			:return: resource_blocks: numeric value"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		allocation_cmd_val = self._cmd_group.get_repcap_cmd_value(allocation, repcap.Allocation)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:SUBFrame{subframe_cmd_val}:ALLoc{allocation_cmd_val}:RBCount?')
		return Conversions.str_to_float(response)
