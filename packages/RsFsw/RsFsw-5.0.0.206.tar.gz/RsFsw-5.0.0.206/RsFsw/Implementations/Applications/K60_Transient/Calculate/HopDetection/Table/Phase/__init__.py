from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Phase:
	"""Phase commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)

	@property
	def all(self):
		"""all commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	@property
	def maxPm(self):
		"""maxPm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maxPm'):
			from .MaxPm import MaxPm
			self._maxPm = MaxPm(self._core, self._cmd_group)
		return self._maxPm

	@property
	def rmsPm(self):
		"""rmsPm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rmsPm'):
			from .RmsPm import RmsPm
			self._rmsPm = RmsPm(self._core, self._cmd_group)
		return self._rmsPm

	@property
	def avgPm(self):
		"""avgPm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_avgPm'):
			from .AvgPm import AvgPm
			self._avgPm = AvgPm(self._core, self._cmd_group)
		return self._avgPm

	def clone(self) -> 'Phase':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Phase(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
