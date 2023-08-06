from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Summary:
	"""Summary commands group definition. 123 total commands, 20 Subgroups, 0 group commands"""

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
	def aapFail(self):
		"""aapFail commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_aapFail'):
			from .AapFail import AapFail
			self._aapFail = AapFail(self._core, self._cmd_group)
		return self._aapFail

	@property
	def apFail(self):
		"""apFail commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_apFail'):
			from .ApFail import ApFail
			self._apFail = ApFail(self._core, self._cmd_group)
		return self._apFail

	@property
	def arpFail(self):
		"""arpFail commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_arpFail'):
			from .ArpFail import ArpFail
			self._arpFail = ArpFail(self._core, self._cmd_group)
		return self._arpFail

	@property
	def evm(self):
		"""evm commands group. 27 Sub-classes, 0 commands."""
		if not hasattr(self, '_evm'):
			from .Evm import Evm
			self._evm = Evm(self._core, self._cmd_group)
		return self._evm

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
	def iqOffset(self):
		"""iqOffset commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOffset'):
			from .IqOffset import IqOffset
			self._iqOffset = IqOffset(self._core, self._cmd_group)
		return self._iqOffset

	@property
	def ostp(self):
		"""ostp commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ostp'):
			from .Ostp import Ostp
			self._ostp = Ostp(self._core, self._cmd_group)
		return self._ostp

	@property
	def power(self):
		"""power commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def quadError(self):
		"""quadError commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_quadError'):
			from .QuadError import QuadError
			self._quadError = QuadError(self._core, self._cmd_group)
		return self._quadError

	@property
	def rsrp(self):
		"""rsrp commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rsrp'):
			from .Rsrp import Rsrp
			self._rsrp = Rsrp(self._core, self._cmd_group)
		return self._rsrp

	@property
	def rstp(self):
		"""rstp commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_rstp'):
			from .Rstp import Rstp
			self._rstp = Rstp(self._core, self._cmd_group)
		return self._rstp

	@property
	def serror(self):
		"""serror commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_serror'):
			from .Serror import Serror
			self._serror = Serror(self._core, self._cmd_group)
		return self._serror

	@property
	def crest(self):
		"""crest commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_crest'):
			from .Crest import Crest
			self._crest = Crest(self._core, self._cmd_group)
		return self._crest

	@property
	def ovld(self):
		"""ovld commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ovld'):
			from .Ovld import Ovld
			self._ovld = Ovld(self._core, self._cmd_group)
		return self._ovld

	@property
	def spDail(self):
		"""spDail commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spDail'):
			from .SpDail import SpDail
			self._spDail = SpDail(self._core, self._cmd_group)
		return self._spDail

	@property
	def sstate(self):
		"""sstate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sstate'):
			from .Sstate import Sstate
			self._sstate = Sstate(self._core, self._cmd_group)
		return self._sstate

	@property
	def tsDelta(self):
		"""tsDelta commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tsDelta'):
			from .TsDelta import TsDelta
			self._tsDelta = TsDelta(self._core, self._cmd_group)
		return self._tsDelta

	@property
	def tstamp(self):
		"""tstamp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tstamp'):
			from .Tstamp import Tstamp
			self._tstamp = Tstamp(self._core, self._cmd_group)
		return self._tstamp

	def clone(self) -> 'Summary':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Summary(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
