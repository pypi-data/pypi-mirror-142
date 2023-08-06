from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PmSettling:
	"""PmSettling commands group definition. 15 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pmSettling", core, parent)

	@property
	def pmSpoint(self):
		"""pmSpoint commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmSpoint'):
			from .PmSpoint import PmSpoint
			self._pmSpoint = PmSpoint(self._core, self._cmd_group)
		return self._pmSpoint

	@property
	def pmStime(self):
		"""pmStime commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmStime'):
			from .PmStime import PmStime
			self._pmStime = PmStime(self._core, self._cmd_group)
		return self._pmStime

	@property
	def pmsLength(self):
		"""pmsLength commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmsLength'):
			from .PmsLength import PmsLength
			self._pmsLength = PmsLength(self._core, self._cmd_group)
		return self._pmsLength

	def clone(self) -> 'PmSettling':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PmSettling(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
