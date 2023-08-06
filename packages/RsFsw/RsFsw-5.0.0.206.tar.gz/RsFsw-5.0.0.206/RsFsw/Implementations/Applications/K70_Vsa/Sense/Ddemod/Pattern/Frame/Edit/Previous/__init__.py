from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Previous:
	"""Previous commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("previous", core, parent)

	@property
	def boosting(self):
		"""boosting commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_boosting'):
			from .Boosting import Boosting
			self._boosting = Boosting(self._core, self._cmd_group)
		return self._boosting

	@property
	def modulation(self):
		"""modulation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import Modulation
			self._modulation = Modulation(self._core, self._cmd_group)
		return self._modulation

	def clone(self) -> 'Previous':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Previous(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
