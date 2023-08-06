from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RbCount:
	"""RbCount commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rbCount", core, parent)

	def set(self, resource_blocks: float, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default, cluster=repcap.Cluster.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:SUBFrame<sf>:ALLoc[:CLUSter<cl>]:RBCount \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.subframe.alloc.cluster.rbCount.set(resource_blocks = 1.0, carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default, cluster = repcap.Cluster.Default) \n
		This command selects the number of resource blocks in an uplink subframe. \n
			:param resource_blocks: numeric value
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
			:param cluster: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cluster')
		"""
		param = Conversions.decimal_value_to_str(resource_blocks)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		cluster_cmd_val = self._cmd_group.get_repcap_cmd_value(cluster, repcap.Cluster)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:SUBFrame{subframe_cmd_val}:ALLoc:CLUSter{cluster_cmd_val}:RBCount {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default, cluster=repcap.Cluster.Default) -> float:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:SUBFrame<sf>:ALLoc[:CLUSter<cl>]:RBCount \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.uplink.cc.subframe.alloc.cluster.rbCount.get(carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default, cluster = repcap.Cluster.Default) \n
		This command selects the number of resource blocks in an uplink subframe. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
			:param cluster: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cluster')
			:return: resource_blocks: numeric value"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		cluster_cmd_val = self._cmd_group.get_repcap_cmd_value(cluster, repcap.Cluster)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:SUBFrame{subframe_cmd_val}:ALLoc:CLUSter{cluster_cmd_val}:RBCount?')
		return Conversions.str_to_float(response)
