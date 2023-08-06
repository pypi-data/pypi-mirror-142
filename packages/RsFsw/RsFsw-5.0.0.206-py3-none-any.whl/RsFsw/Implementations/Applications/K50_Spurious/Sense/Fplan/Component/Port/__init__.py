from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Port:
	"""Port commands group definition. 2 total commands, 2 Subgroups, 0 group commands
	Repeated Capability: Port, default value after init: Port.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("port", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_port_get', 'repcap_port_set', repcap.Port.Nr1)

	def repcap_port_set(self, port: repcap.Port) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Port.Default
		Default value after init: Port.Nr1"""
		self._cmd_group.set_repcap_enum_value(port)

	def repcap_port_get(self) -> repcap.Port:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def mharmonic(self):
		"""mharmonic commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mharmonic'):
			from .Mharmonic import Mharmonic
			self._mharmonic = Mharmonic(self._core, self._cmd_group)
		return self._mharmonic

	def clone(self) -> 'Port':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Port(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
