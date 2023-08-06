from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 28 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	@property
	def channel(self):
		"""channel commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_channel'):
			from .Channel import Channel
			self._channel = Channel(self._core, self._cmd_group)
		return self._channel

	@property
	def item(self):
		"""item commands group. 16 Sub-classes, 0 commands."""
		if not hasattr(self, '_item'):
			from .Item import Item
			self._item = Item(self._core, self._cmd_group)
		return self._item

	def clone(self) -> 'Select':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Select(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
