from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scapture:
	"""Scapture commands group definition. 3 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scapture", core, parent)

	@property
	def boundary(self):
		"""boundary commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_boundary'):
			from .Boundary import Boundary
			self._boundary = Boundary(self._core, self._cmd_group)
		return self._boundary

	@property
	def tstamp(self):
		"""tstamp commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tstamp'):
			from .Tstamp import Tstamp
			self._tstamp = Tstamp(self._core, self._cmd_group)
		return self._tstamp

	def clone(self) -> 'Scapture':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Scapture(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
