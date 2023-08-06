from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 6 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	@property
	def absolute(self):
		"""absolute commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_absolute'):
			from .Absolute import Absolute
			self._absolute = Absolute(self._core, self._cmd_group)
		return self._absolute

	@property
	def caclr(self):
		"""caclr commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_caclr'):
			from .Caclr import Caclr
			self._caclr = Caclr(self._core, self._cmd_group)
		return self._caclr

	@property
	def aclr(self):
		"""aclr commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_aclr'):
			from .Aclr import Aclr
			self._aclr = Aclr(self._core, self._cmd_group)
		return self._aclr

	def clone(self) -> 'Auto':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Auto(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
