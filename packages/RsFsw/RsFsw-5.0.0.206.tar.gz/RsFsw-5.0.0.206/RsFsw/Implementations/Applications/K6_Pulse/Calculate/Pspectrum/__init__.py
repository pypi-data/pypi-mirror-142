from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pspectrum:
	"""Pspectrum commands group definition. 13 total commands, 13 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pspectrum", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	@property
	def maxFrequency(self):
		"""maxFrequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_maxFrequency'):
			from .MaxFrequency import MaxFrequency
			self._maxFrequency = MaxFrequency(self._core, self._cmd_group)
		return self._maxFrequency

	@property
	def window(self):
		"""window commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_window'):
			from .Window import Window
			self._window = Window(self._core, self._cmd_group)
		return self._window

	@property
	def blockSize(self):
		"""blockSize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_blockSize'):
			from .BlockSize import BlockSize
			self._blockSize = BlockSize(self._core, self._cmd_group)
		return self._blockSize

	@property
	def gthreshold(self):
		"""gthreshold commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gthreshold'):
			from .Gthreshold import Gthreshold
			self._gthreshold = Gthreshold(self._core, self._cmd_group)
		return self._gthreshold

	@property
	def sthreshold(self):
		"""sthreshold commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sthreshold'):
			from .Sthreshold import Sthreshold
			self._sthreshold = Sthreshold(self._core, self._cmd_group)
		return self._sthreshold

	@property
	def rbw(self):
		"""rbw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rbw'):
			from .Rbw import Rbw
			self._rbw = Rbw(self._core, self._cmd_group)
		return self._rbw

	@property
	def frequency(self):
		"""frequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

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

	def clone(self) -> 'Pspectrum':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pspectrum(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
