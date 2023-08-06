from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Summary:
	"""Summary commands group definition. 45 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("summary", core, parent)

	@property
	def evm(self):
		"""evm commands group. 27 Sub-classes, 0 commands."""
		if not hasattr(self, '_evm'):
			from .Evm import Evm
			self._evm = Evm(self._core, self._cmd_group)
		return self._evm

	@property
	def freqError(self):
		"""freqError commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_freqError'):
			from .FreqError import FreqError
			self._freqError = FreqError(self._core, self._cmd_group)
		return self._freqError

	@property
	def gimbalance(self):
		"""gimbalance commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gimbalance'):
			from .Gimbalance import Gimbalance
			self._gimbalance = Gimbalance(self._core, self._cmd_group)
		return self._gimbalance

	@property
	def iqOffset(self):
		"""iqOffset commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOffset'):
			from .IqOffset import IqOffset
			self._iqOffset = IqOffset(self._core, self._cmd_group)
		return self._iqOffset

	@property
	def quadError(self):
		"""quadError commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_quadError'):
			from .QuadError import QuadError
			self._quadError = QuadError(self._core, self._cmd_group)
		return self._quadError

	@property
	def serror(self):
		"""serror commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_serror'):
			from .Serror import Serror
			self._serror = Serror(self._core, self._cmd_group)
		return self._serror

	def clone(self) -> 'Summary':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Summary(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
