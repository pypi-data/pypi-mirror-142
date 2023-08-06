from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spurs:
	"""Spurs commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spurs", core, parent)

	@property
	def suppress(self):
		"""suppress commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_suppress'):
			from .Suppress import Suppress
			self._suppress = Suppress(self._core, self._cmd_group)
		return self._suppress

	@property
	def threshold(self):
		"""threshold commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_threshold'):
			from .Threshold import Threshold
			self._threshold = Threshold(self._core, self._cmd_group)
		return self._threshold

	def clone(self) -> 'Spurs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Spurs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
