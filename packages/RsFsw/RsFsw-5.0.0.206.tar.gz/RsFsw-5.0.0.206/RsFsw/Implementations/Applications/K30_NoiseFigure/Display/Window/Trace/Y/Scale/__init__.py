from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scale:
	"""Scale commands group definition. 5 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scale", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	@property
	def bottom(self):
		"""bottom commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bottom'):
			from .Bottom import Bottom
			self._bottom = Bottom(self._core, self._cmd_group)
		return self._bottom

	@property
	def refLevel(self):
		"""refLevel commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_refLevel'):
			from .RefLevel import RefLevel
			self._refLevel = RefLevel(self._core, self._cmd_group)
		return self._refLevel

	@property
	def top(self):
		"""top commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_top'):
			from .Top import Top
			self._top = Top(self._core, self._cmd_group)
		return self._top

	def clone(self) -> 'Scale':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scale(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
