from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.RepeatedCapability import RepeatedCapability
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Probe:
	"""Probe commands group definition. 13 total commands, 2 Subgroups, 0 group commands
	Repeated Capability: Probe, default value after init: Probe.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("probe", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_probe_get', 'repcap_probe_set', repcap.Probe.Nr1)

	def repcap_probe_set(self, probe: repcap.Probe) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Probe.Default
		Default value after init: Probe.Nr1"""
		self._cmd_group.set_repcap_enum_value(probe)

	def repcap_probe_get(self) -> repcap.Probe:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def id(self):
		"""id commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_id'):
			from .Id import Id
			self._id = Id(self._core, self._cmd_group)
		return self._id

	@property
	def setup(self):
		"""setup commands group. 11 Sub-classes, 0 commands."""
		if not hasattr(self, '_setup'):
			from .Setup import Setup
			self._setup = Setup(self._core, self._cmd_group)
		return self._setup

	def clone(self) -> 'Probe':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Probe(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
