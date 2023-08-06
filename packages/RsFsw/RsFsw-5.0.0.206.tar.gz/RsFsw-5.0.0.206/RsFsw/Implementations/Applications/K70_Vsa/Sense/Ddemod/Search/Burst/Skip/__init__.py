from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Skip:
	"""Skip commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("skip", core, parent)

	@property
	def rising(self):
		"""rising commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rising'):
			from .Rising import Rising
			self._rising = Rising(self._core, self._cmd_group)
		return self._rising

	@property
	def falling(self):
		"""falling commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_falling'):
			from .Falling import Falling
			self._falling = Falling(self._core, self._cmd_group)
		return self._falling

	def clone(self) -> 'Skip':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Skip(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
