from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 30 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def fmError(self):
		"""fmError commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_fmError'):
			from .FmError import FmError
			self._fmError = FmError(self._core, self._cmd_group)
		return self._fmError

	@property
	def maxFm(self):
		"""maxFm commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_maxFm'):
			from .MaxFm import MaxFm
			self._maxFm = MaxFm(self._core, self._cmd_group)
		return self._maxFm

	@property
	def rmsFm(self):
		"""rmsFm commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_rmsFm'):
			from .RmsFm import RmsFm
			self._rmsFm = RmsFm(self._core, self._cmd_group)
		return self._rmsFm

	@property
	def avgFm(self):
		"""avgFm commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_avgFm'):
			from .AvgFm import AvgFm
			self._avgFm = AvgFm(self._core, self._cmd_group)
		return self._avgFm

	@property
	def relFrequency(self):
		"""relFrequency commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_relFrequency'):
			from .RelFrequency import RelFrequency
			self._relFrequency = RelFrequency(self._core, self._cmd_group)
		return self._relFrequency

	def clone(self) -> 'Frequency':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Frequency(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
