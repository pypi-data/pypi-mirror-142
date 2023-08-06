from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Network:
	"""Network commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("network", core, parent)

	@property
	def unusedDrives(self):
		"""unusedDrives commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_unusedDrives'):
			from .UnusedDrives import UnusedDrives
			self._unusedDrives = UnusedDrives(self._core, self._cmd_group)
		return self._unusedDrives

	@property
	def map(self):
		"""map commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_map'):
			from .Map import Map
			self._map = Map(self._core, self._cmd_group)
		return self._map

	@property
	def disconnect(self):
		"""disconnect commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_disconnect'):
			from .Disconnect import Disconnect
			self._disconnect = Disconnect(self._core, self._cmd_group)
		return self._disconnect

	@property
	def usedDrives(self):
		"""usedDrives commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_usedDrives'):
			from .UsedDrives import UsedDrives
			self._usedDrives = UsedDrives(self._core, self._cmd_group)
		return self._usedDrives

	def clone(self) -> 'Network':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Network(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
