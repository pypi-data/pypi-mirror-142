from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class System:
	"""System commands group definition. 3 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("system", core, parent)

	@property
	def lo(self):
		"""lo commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_lo'):
			from .Lo import Lo
			self._lo = Lo(self._core, self._cmd_group)
		return self._lo

	@property
	def ifreq(self):
		"""ifreq commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ifreq'):
			from .Ifreq import Ifreq
			self._ifreq = Ifreq(self._core, self._cmd_group)
		return self._ifreq

	def clone(self) -> 'System':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = System(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
