from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Preset:
	"""Preset commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("preset", core, parent)

	@property
	def exec(self):
		"""exec commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_exec'):
			from .Exec import Exec
			self._exec = Exec(self._core, self._cmd_group)
		return self._exec

	@property
	def compatible(self):
		"""compatible commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_compatible'):
			from .Compatible import Compatible
			self._compatible = Compatible(self._core, self._cmd_group)
		return self._compatible

	@property
	def channel(self):
		"""channel commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_channel'):
			from .Channel import Channel
			self._channel = Channel(self._core, self._cmd_group)
		return self._channel

	def clone(self) -> 'Preset':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Preset(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
