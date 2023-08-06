from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Configure:
	"""Configure commands group definition. 12 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("configure", core, parent)

	@property
	def correction(self):
		"""correction commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_correction'):
			from .Correction import Correction
			self._correction = Correction(self._core, self._cmd_group)
		return self._correction

	@property
	def frequency(self):
		"""frequency commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def listPy(self):
		"""listPy commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPy
			self._listPy = ListPy(self._core, self._cmd_group)
		return self._listPy

	@property
	def single(self):
		"""single commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_single'):
			from .Single import Single
			self._single = Single(self._core, self._cmd_group)
		return self._single

	@property
	def mode(self):
		"""mode commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def control(self):
		"""control commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_control'):
			from .Control import Control
			self._control = Control(self._core, self._cmd_group)
		return self._control

	@property
	def measurement(self):
		"""measurement commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_measurement'):
			from .Measurement import Measurement
			self._measurement = Measurement(self._core, self._cmd_group)
		return self._measurement

	def clone(self) -> 'Configure':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Configure(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
