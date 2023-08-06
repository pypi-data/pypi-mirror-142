from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Output:
	"""Output commands group definition. 7 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("output", core, parent)

	@property
	def ifreq(self):
		"""ifreq commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ifreq'):
			from .Ifreq import Ifreq
			self._ifreq = Ifreq(self._core, self._cmd_group)
		return self._ifreq

	@property
	def trigger(self):
		"""trigger commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_trigger'):
			from .Trigger import Trigger
			self._trigger = Trigger(self._core, self._cmd_group)
		return self._trigger

	def clone(self) -> 'Output':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Output(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
