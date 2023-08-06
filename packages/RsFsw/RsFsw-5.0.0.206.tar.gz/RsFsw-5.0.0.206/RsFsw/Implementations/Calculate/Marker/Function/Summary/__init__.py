from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Summary:
	"""Summary commands group definition. 20 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("summary", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def ppeak(self):
		"""ppeak commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_ppeak'):
			from .Ppeak import Ppeak
			self._ppeak = Ppeak(self._core, self._cmd_group)
		return self._ppeak

	@property
	def rms(self):
		"""rms commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_rms'):
			from .Rms import Rms
			self._rms = Rms(self._core, self._cmd_group)
		return self._rms

	@property
	def mean(self):
		"""mean commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_mean'):
			from .Mean import Mean
			self._mean = Mean(self._core, self._cmd_group)
		return self._mean

	@property
	def standardDev(self):
		"""standardDev commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_standardDev'):
			from .StandardDev import StandardDev
			self._standardDev = StandardDev(self._core, self._cmd_group)
		return self._standardDev

	@property
	def phold(self):
		"""phold commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phold'):
			from .Phold import Phold
			self._phold = Phold(self._core, self._cmd_group)
		return self._phold

	@property
	def average(self):
		"""average commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_average'):
			from .Average import Average
			self._average = Average(self._core, self._cmd_group)
		return self._average

	@property
	def aoff(self):
		"""aoff commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aoff'):
			from .Aoff import Aoff
			self._aoff = Aoff(self._core, self._cmd_group)
		return self._aoff

	def clone(self) -> 'Summary':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Summary(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
