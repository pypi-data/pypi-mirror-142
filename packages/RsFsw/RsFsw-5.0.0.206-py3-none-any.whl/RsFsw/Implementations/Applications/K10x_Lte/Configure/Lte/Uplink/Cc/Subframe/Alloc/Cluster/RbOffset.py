from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RbOffset:
	"""RbOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rbOffset", core, parent)

	def set(self, offset: float, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default, cluster=repcap.Cluster.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:SUBFrame<sf>:ALLoc[:CLUSter<cl>]:RBOFfset \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.subframe.alloc.cluster.rbOffset.set(offset = 1.0, carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default, cluster = repcap.Cluster.Default) \n
		This command defines the resource block offset in an uplink subframe. \n
			:param offset: numeric value
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
			:param cluster: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cluster')
		"""
		param = Conversions.decimal_value_to_str(offset)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		cluster_cmd_val = self._cmd_group.get_repcap_cmd_value(cluster, repcap.Cluster)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:SUBFrame{subframe_cmd_val}:ALLoc:CLUSter{cluster_cmd_val}:RBOFfset {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default, cluster=repcap.Cluster.Default) -> float:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:SUBFrame<sf>:ALLoc[:CLUSter<cl>]:RBOFfset \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.uplink.cc.subframe.alloc.cluster.rbOffset.get(carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default, cluster = repcap.Cluster.Default) \n
		This command defines the resource block offset in an uplink subframe. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
			:param cluster: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cluster')
			:return: offset: numeric value"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		cluster_cmd_val = self._cmd_group.get_repcap_cmd_value(cluster, repcap.Cluster)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:SUBFrame{subframe_cmd_val}:ALLoc:CLUSter{cluster_cmd_val}:RBOFfset?')
		return Conversions.str_to_float(response)
