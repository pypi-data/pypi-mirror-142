from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Packet:
	"""Packet commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("packet", core, parent)

	@property
	def count(self):
		"""count commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Count import Count
			self._count = Count(self._core, self._cmd_group)
		return self._count

	@property
	def group(self):
		"""group commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_group'):
			from .Group import Group
			self._group = Group(self._core, self._cmd_group)
		return self._group

	@property
	def number(self):
		"""number commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_number'):
			from .Number import Number
			self._number = Number(self._core, self._cmd_group)
		return self._number

	def clone(self) -> 'Packet':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Packet(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
