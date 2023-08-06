from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Arbitrary:
	"""Arbitrary commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("arbitrary", core, parent)

	@property
	def clock(self):
		"""clock commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_clock'):
			from .Clock import Clock
			self._clock = Clock(self._core, self._cmd_group)
		return self._clock

	@property
	def tsignal(self):
		"""tsignal commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tsignal'):
			from .Tsignal import Tsignal
			self._tsignal = Tsignal(self._core, self._cmd_group)
		return self._tsignal

	@property
	def waveform(self):
		"""waveform commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_waveform'):
			from .Waveform import Waveform
			self._waveform = Waveform(self._core, self._cmd_group)
		return self._waveform

	def clone(self) -> 'Arbitrary':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Arbitrary(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
