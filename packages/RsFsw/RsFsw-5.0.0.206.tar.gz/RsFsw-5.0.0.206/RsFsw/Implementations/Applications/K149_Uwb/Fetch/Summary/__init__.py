from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Summary:
	"""Summary commands group definition. 131 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("summary", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	@property
	def evm(self):
		"""evm commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_evm'):
			from .Evm import Evm
			self._evm = Evm(self._core, self._cmd_group)
		return self._evm

	@property
	def frequency(self):
		"""frequency commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def jitter(self):
		"""jitter commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_jitter'):
			from .Jitter import Jitter
			self._jitter = Jitter(self._core, self._cmd_group)
		return self._jitter

	@property
	def power(self):
		"""power commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def pulse(self):
		"""pulse commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pulse'):
			from .Pulse import Pulse
			self._pulse = Pulse(self._core, self._cmd_group)
		return self._pulse

	@property
	def ranging(self):
		"""ranging commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ranging'):
			from .Ranging import Ranging
			self._ranging = Ranging(self._core, self._cmd_group)
		return self._ranging

	@property
	def spectrum(self):
		"""spectrum commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_spectrum'):
			from .Spectrum import Spectrum
			self._spectrum = Spectrum(self._core, self._cmd_group)
		return self._spectrum

	@property
	def xcorr(self):
		"""xcorr commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_xcorr'):
			from .Xcorr import Xcorr
			self._xcorr = Xcorr(self._core, self._cmd_group)
		return self._xcorr

	def clone(self) -> 'Summary':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Summary(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
