from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ademod:
	"""Ademod commands group definition. 14 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ademod", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def mcPhase(self):
		"""mcPhase commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_mcPhase'):
			from .McPhase import McPhase
			self._mcPhase = McPhase(self._core, self._cmd_group)
		return self._mcPhase

	@property
	def spectrum(self):
		"""spectrum commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_spectrum'):
			from .Spectrum import Spectrum
			self._spectrum = Spectrum(self._core, self._cmd_group)
		return self._spectrum

	@property
	def bandwidth(self):
		"""bandwidth commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import Bandwidth
			self._bandwidth = Bandwidth(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def mtime(self):
		"""mtime commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mtime'):
			from .Mtime import Mtime
			self._mtime = Mtime(self._core, self._cmd_group)
		return self._mtime

	@property
	def rlength(self):
		"""rlength commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rlength'):
			from .Rlength import Rlength
			self._rlength = Rlength(self._core, self._cmd_group)
		return self._rlength

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRate
			self._symbolRate = SymbolRate(self._core, self._cmd_group)
		return self._symbolRate

	def clone(self) -> 'Ademod':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ademod(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
