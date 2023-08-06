from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 10 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	@property
	def all(self):
		"""all commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	@property
	def avgFm(self):
		"""avgFm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_avgFm'):
			from .AvgFm import AvgFm
			self._avgFm = AvgFm(self._core, self._cmd_group)
		return self._avgFm

	@property
	def avgNonlinear(self):
		"""avgNonlinear commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_avgNonlinear'):
			from .AvgNonlinear import AvgNonlinear
			self._avgNonlinear = AvgNonlinear(self._core, self._cmd_group)
		return self._avgNonlinear

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import Bandwidth
			self._bandwidth = Bandwidth(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def chError(self):
		"""chError commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_chError'):
			from .ChError import ChError
			self._chError = ChError(self._core, self._cmd_group)
		return self._chError

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def maxFm(self):
		"""maxFm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maxFm'):
			from .MaxFm import MaxFm
			self._maxFm = MaxFm(self._core, self._cmd_group)
		return self._maxFm

	@property
	def maxNonlinear(self):
		"""maxNonlinear commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maxNonlinear'):
			from .MaxNonlinear import MaxNonlinear
			self._maxNonlinear = MaxNonlinear(self._core, self._cmd_group)
		return self._maxNonlinear

	@property
	def rmsFm(self):
		"""rmsFm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rmsFm'):
			from .RmsFm import RmsFm
			self._rmsFm = RmsFm(self._core, self._cmd_group)
		return self._rmsFm

	@property
	def rmsNonlinear(self):
		"""rmsNonlinear commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rmsNonlinear'):
			from .RmsNonlinear import RmsNonlinear
			self._rmsNonlinear = RmsNonlinear(self._core, self._cmd_group)
		return self._rmsNonlinear

	def clone(self) -> 'Frequency':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Frequency(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
