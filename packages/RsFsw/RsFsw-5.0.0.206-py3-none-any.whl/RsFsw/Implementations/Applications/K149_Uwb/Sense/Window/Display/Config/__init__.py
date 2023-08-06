from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Config:
	"""Config commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("config", core, parent)

	@property
	def bins(self):
		"""bins commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bins'):
			from .Bins import Bins
			self._bins = Bins(self._core, self._cmd_group)
		return self._bins

	@property
	def scale(self):
		"""scale commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scale'):
			from .Scale import Scale
			self._scale = Scale(self._core, self._cmd_group)
		return self._scale

	@property
	def section(self):
		"""section commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_section'):
			from .Section import Section
			self._section = Section(self._core, self._cmd_group)
		return self._section

	def clone(self) -> 'Config':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Config(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
