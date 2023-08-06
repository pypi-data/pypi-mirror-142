from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maccuracy:
	"""Maccuracy commands group definition. 35 total commands, 13 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maccuracy", core, parent)

	@property
	def adroop(self):
		"""adroop commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_adroop'):
			from .Adroop import Adroop
			self._adroop = Adroop(self._core, self._cmd_group)
		return self._adroop

	@property
	def freqError(self):
		"""freqError commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_freqError'):
			from .FreqError import FreqError
			self._freqError = FreqError(self._core, self._cmd_group)
		return self._freqError

	@property
	def gimbalance(self):
		"""gimbalance commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_gimbalance'):
			from .Gimbalance import Gimbalance
			self._gimbalance = Gimbalance(self._core, self._cmd_group)
		return self._gimbalance

	@property
	def iqImbalance(self):
		"""iqImbalance commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqImbalance'):
			from .IqImbalance import IqImbalance
			self._iqImbalance = IqImbalance(self._core, self._cmd_group)
		return self._iqImbalance

	@property
	def iqOffset(self):
		"""iqOffset commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOffset'):
			from .IqOffset import IqOffset
			self._iqOffset = IqOffset(self._core, self._cmd_group)
		return self._iqOffset

	@property
	def merror(self):
		"""merror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_merror'):
			from .Merror import Merror
			self._merror = Merror(self._core, self._cmd_group)
		return self._merror

	@property
	def perror(self):
		"""perror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_perror'):
			from .Perror import Perror
			self._perror = Perror(self._core, self._cmd_group)
		return self._perror

	@property
	def qerror(self):
		"""qerror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_qerror'):
			from .Qerror import Qerror
			self._qerror = Qerror(self._core, self._cmd_group)
		return self._qerror

	@property
	def result(self):
		"""result commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_result'):
			from .Result import Result
			self._result = Result(self._core, self._cmd_group)
		return self._result

	@property
	def revm(self):
		"""revm commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_revm'):
			from .Revm import Revm
			self._revm = Revm(self._core, self._cmd_group)
		return self._revm

	@property
	def rmev(self):
		"""rmev commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_rmev'):
			from .Rmev import Rmev
			self._rmev = Rmev(self._core, self._cmd_group)
		return self._rmev

	@property
	def srError(self):
		"""srError commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_srError'):
			from .SrError import SrError
			self._srError = SrError(self._core, self._cmd_group)
		return self._srError

	@property
	def poffset(self):
		"""poffset commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_poffset'):
			from .Poffset import Poffset
			self._poffset = Poffset(self._core, self._cmd_group)
		return self._poffset

	def clone(self) -> 'Maccuracy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Maccuracy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
