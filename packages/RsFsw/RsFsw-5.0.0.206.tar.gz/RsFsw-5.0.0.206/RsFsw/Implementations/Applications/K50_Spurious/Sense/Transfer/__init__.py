from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Transfer:
	"""Transfer commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("transfer", core, parent)

	@property
	def segment(self):
		"""segment commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_segment'):
			from .Segment import Segment
			self._segment = Segment(self._core, self._cmd_group)
		return self._segment

	@property
	def spur(self):
		"""spur commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spur'):
			from .Spur import Spur
			self._spur = Spur(self._core, self._cmd_group)
		return self._spur

	def clone(self) -> 'Transfer':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Transfer(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
