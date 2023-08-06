from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Page:
	"""Page commands group definition. 11 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("page", core, parent)

	@property
	def orientation(self):
		"""orientation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_orientation'):
			from .Orientation import Orientation
			self._orientation = Orientation(self._core, self._cmd_group)
		return self._orientation

	@property
	def margin(self):
		"""margin commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_margin'):
			from .Margin import Margin
			self._margin = Margin(self._core, self._cmd_group)
		return self._margin

	@property
	def count(self):
		"""count commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_count'):
			from .Count import Count
			self._count = Count(self._core, self._cmd_group)
		return self._count

	@property
	def window(self):
		"""window commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_window'):
			from .Window import Window
			self._window = Window(self._core, self._cmd_group)
		return self._window

	def clone(self) -> 'Page':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Page(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
