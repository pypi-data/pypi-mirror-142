from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Distribution:
	"""Distribution commands group definition. 8 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("distribution", core, parent)

	@property
	def llines(self):
		"""llines commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_llines'):
			from .Llines import Llines
			self._llines = Llines(self._core, self._cmd_group)
		return self._llines

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def nbins(self):
		"""nbins commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nbins'):
			from .Nbins import Nbins
			self._nbins = Nbins(self._core, self._cmd_group)
		return self._nbins

	@property
	def phase(self):
		"""phase commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phase'):
			from .Phase import Phase
			self._phase = Phase(self._core, self._cmd_group)
		return self._phase

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def timing(self):
		"""timing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_timing'):
			from .Timing import Timing
			self._timing = Timing(self._core, self._cmd_group)
		return self._timing

	@property
	def emodel(self):
		"""emodel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_emodel'):
			from .Emodel import Emodel
			self._emodel = Emodel(self._core, self._cmd_group)
		return self._emodel

	@property
	def tsidelobe(self):
		"""tsidelobe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tsidelobe'):
			from .Tsidelobe import Tsidelobe
			self._tsidelobe = Tsidelobe(self._core, self._cmd_group)
		return self._tsidelobe

	def clone(self) -> 'Distribution':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Distribution(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
