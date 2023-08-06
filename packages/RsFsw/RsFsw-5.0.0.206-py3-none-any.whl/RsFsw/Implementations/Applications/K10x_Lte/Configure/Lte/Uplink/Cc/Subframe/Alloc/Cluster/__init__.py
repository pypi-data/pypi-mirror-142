from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal.RepeatedCapability import RepeatedCapability
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cluster:
	"""Cluster commands group definition. 2 total commands, 2 Subgroups, 0 group commands
	Repeated Capability: Cluster, default value after init: Cluster.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cluster", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_cluster_get', 'repcap_cluster_set', repcap.Cluster.Nr1)

	def repcap_cluster_set(self, cluster: repcap.Cluster) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Cluster.Default
		Default value after init: Cluster.Nr1"""
		self._cmd_group.set_repcap_enum_value(cluster)

	def repcap_cluster_get(self) -> repcap.Cluster:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def rbCount(self):
		"""rbCount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbCount'):
			from .RbCount import RbCount
			self._rbCount = RbCount(self._core, self._cmd_group)
		return self._rbCount

	@property
	def rbOffset(self):
		"""rbOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbOffset'):
			from .RbOffset import RbOffset
			self._rbOffset = RbOffset(self._core, self._cmd_group)
		return self._rbOffset

	def clone(self) -> 'Cluster':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cluster(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
