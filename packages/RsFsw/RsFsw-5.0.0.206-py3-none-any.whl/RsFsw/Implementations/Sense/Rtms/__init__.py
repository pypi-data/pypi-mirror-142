from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rtms:
	"""Rtms commands group definition. 1 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rtms", core, parent)

	@property
	def capture(self):
		"""capture commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_capture'):
			from .Capture import Capture
			self._capture = Capture(self._core, self._cmd_group)
		return self._capture

	def clone(self) -> 'Rtms':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rtms(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
