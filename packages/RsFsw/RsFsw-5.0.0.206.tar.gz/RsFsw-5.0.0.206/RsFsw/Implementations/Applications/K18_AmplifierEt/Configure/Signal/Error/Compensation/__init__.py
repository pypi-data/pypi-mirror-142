from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Compensation:
	"""Compensation commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("compensation", core, parent)

	@property
	def adroop(self):
		"""adroop commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_adroop'):
			from .Adroop import Adroop
			self._adroop = Adroop(self._core, self._cmd_group)
		return self._adroop

	@property
	def freqError(self):
		"""freqError commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_freqError'):
			from .FreqError import FreqError
			self._freqError = FreqError(self._core, self._cmd_group)
		return self._freqError

	@property
	def iqOffset(self):
		"""iqOffset commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOffset'):
			from .IqOffset import IqOffset
			self._iqOffset = IqOffset(self._core, self._cmd_group)
		return self._iqOffset

	@property
	def iqImbalance(self):
		"""iqImbalance commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqImbalance'):
			from .IqImbalance import IqImbalance
			self._iqImbalance = IqImbalance(self._core, self._cmd_group)
		return self._iqImbalance

	@property
	def symbolRate(self):
		"""symbolRate commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRate
			self._symbolRate = SymbolRate(self._core, self._cmd_group)
		return self._symbolRate

	def clone(self) -> 'Compensation':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Compensation(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
