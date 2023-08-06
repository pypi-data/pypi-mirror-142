from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ccir:
	"""Ccir commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ccir", core, parent)

	@property
	def unweighted(self):
		"""unweighted commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_unweighted'):
			from .Unweighted import Unweighted
			self._unweighted = Unweighted(self._core, self._cmd_group)
		return self._unweighted

	@property
	def weighted(self):
		"""weighted commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_weighted'):
			from .Weighted import Weighted
			self._weighted = Weighted(self._core, self._cmd_group)
		return self._weighted

	def clone(self) -> 'Ccir':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ccir(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
