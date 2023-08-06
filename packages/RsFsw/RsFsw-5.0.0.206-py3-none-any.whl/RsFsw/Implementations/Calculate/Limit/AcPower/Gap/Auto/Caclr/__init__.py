from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Caclr:
	"""Caclr commands group definition. 2 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("caclr", core, parent)

	@property
	def relative(self):
		"""relative commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_relative'):
			from .Relative import Relative
			self._relative = Relative(self._core, self._cmd_group)
		return self._relative

	def clone(self) -> 'Caclr':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Caclr(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
