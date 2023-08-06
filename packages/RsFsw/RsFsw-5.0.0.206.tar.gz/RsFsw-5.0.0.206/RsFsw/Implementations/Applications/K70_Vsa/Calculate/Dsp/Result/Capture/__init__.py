from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Capture:
	"""Capture commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("capture", core, parent)

	@property
	def bursts(self):
		"""bursts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bursts'):
			from .Bursts import Bursts
			self._bursts = Bursts(self._core, self._cmd_group)
		return self._bursts

	@property
	def patterns(self):
		"""patterns commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_patterns'):
			from .Patterns import Patterns
			self._patterns = Patterns(self._core, self._cmd_group)
		return self._patterns

	def clone(self) -> 'Capture':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Capture(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
