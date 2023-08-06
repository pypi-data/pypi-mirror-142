from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Precoding:
	"""Precoding commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("precoding", core, parent)

	@property
	def cbIndex(self):
		"""cbIndex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbIndex'):
			from .CbIndex import CbIndex
			self._cbIndex = CbIndex(self._core, self._cmd_group)
		return self._cbIndex

	@property
	def clMapping(self):
		"""clMapping commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_clMapping'):
			from .ClMapping import ClMapping
			self._clMapping = ClMapping(self._core, self._cmd_group)
		return self._clMapping

	def clone(self) -> 'Precoding':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Precoding(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
