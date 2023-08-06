from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Summary:
	"""Summary commands group definition. 93 total commands, 15 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("summary", core, parent)

	@property
	def crest(self):
		"""crest commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_crest'):
			from .Crest import Crest
			self._crest = Crest(self._core, self._cmd_group)
		return self._crest

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
	def rbp(self):
		"""rbp commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_rbp'):
			from .Rbp import Rbp
			self._rbp = Rbp(self._core, self._cmd_group)
		return self._rbp

	@property
	def nbPower(self):
		"""nbPower commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_nbPower'):
			from .NbPower import NbPower
			self._nbPower = NbPower(self._core, self._cmd_group)
		return self._nbPower

	@property
	def rfError(self):
		"""rfError commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfError'):
			from .RfError import RfError
			self._rfError = RfError(self._core, self._cmd_group)
		return self._rfError

	@property
	def rssi(self):
		"""rssi commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_rssi'):
			from .Rssi import Rssi
			self._rssi = Rssi(self._core, self._cmd_group)
		return self._rssi

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
	def tframe(self):
		"""tframe commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tframe'):
			from .Tframe import Tframe
			self._tframe = Tframe(self._core, self._cmd_group)
		return self._tframe

	def clone(self) -> 'Summary':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Summary(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
