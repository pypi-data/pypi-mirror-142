from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stable:
	"""Stable commands group definition. 260 total commands, 27 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stable", core, parent)

	@property
	def amam(self):
		"""amam commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_amam'):
			from .Amam import Amam
			self._amam = Amam(self._core, self._cmd_group)
		return self._amam

	@property
	def amPm(self):
		"""amPm commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_amPm'):
			from .AmPm import AmPm
			self._amPm = AmPm(self._core, self._cmd_group)
		return self._amPm

	@property
	def apae(self):
		"""apae commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_apae'):
			from .Apae import Apae
			self._apae = Apae(self._core, self._cmd_group)
		return self._apae

	@property
	def bbPower(self):
		"""bbPower commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_bbPower'):
			from .BbPower import BbPower
			self._bbPower = BbPower(self._core, self._cmd_group)
		return self._bbPower

	@property
	def icc(self):
		"""icc commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_icc'):
			from .Icc import Icc
			self._icc = Icc(self._core, self._cmd_group)
		return self._icc

	@property
	def ivoltage(self):
		"""ivoltage commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ivoltage'):
			from .Ivoltage import Ivoltage
			self._ivoltage = Ivoltage(self._core, self._cmd_group)
		return self._ivoltage

	@property
	def vcc(self):
		"""vcc commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_vcc'):
			from .Vcc import Vcc
			self._vcc = Vcc(self._core, self._cmd_group)
		return self._vcc

	@property
	def qvoltage(self):
		"""qvoltage commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_qvoltage'):
			from .Qvoltage import Qvoltage
			self._qvoltage = Qvoltage(self._core, self._cmd_group)
		return self._qvoltage

	@property
	def adroop(self):
		"""adroop commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_adroop'):
			from .Adroop import Adroop
			self._adroop = Adroop(self._core, self._cmd_group)
		return self._adroop

	@property
	def freqError(self):
		"""freqError commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_freqError'):
			from .FreqError import FreqError
			self._freqError = FreqError(self._core, self._cmd_group)
		return self._freqError

	@property
	def gimbalance(self):
		"""gimbalance commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_gimbalance'):
			from .Gimbalance import Gimbalance
			self._gimbalance = Gimbalance(self._core, self._cmd_group)
		return self._gimbalance

	@property
	def iqImbalance(self):
		"""iqImbalance commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqImbalance'):
			from .IqImbalance import IqImbalance
			self._iqImbalance = IqImbalance(self._core, self._cmd_group)
		return self._iqImbalance

	@property
	def iqOffset(self):
		"""iqOffset commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqOffset'):
			from .IqOffset import IqOffset
			self._iqOffset = IqOffset(self._core, self._cmd_group)
		return self._iqOffset

	@property
	def merror(self):
		"""merror commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_merror'):
			from .Merror import Merror
			self._merror = Merror(self._core, self._cmd_group)
		return self._merror

	@property
	def perror(self):
		"""perror commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_perror'):
			from .Perror import Perror
			self._perror = Perror(self._core, self._cmd_group)
		return self._perror

	@property
	def power(self):
		"""power commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def qerror(self):
		"""qerror commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_qerror'):
			from .Qerror import Qerror
			self._qerror = Qerror(self._core, self._cmd_group)
		return self._qerror

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
		"""srError commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_srError'):
			from .SrError import SrError
			self._srError = SrError(self._core, self._cmd_group)
		return self._srError

	@property
	def pc(self):
		"""pc commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_pc'):
			from .Pc import Pc
			self._pc = Pc(self._core, self._cmd_group)
		return self._pc

	@property
	def pcpa(self):
		"""pcpa commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcpa'):
			from .Pcpa import Pcpa
			self._pcpa = Pcpa(self._core, self._cmd_group)
		return self._pcpa

	@property
	def cfactor(self):
		"""cfactor commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cfactor'):
			from .Cfactor import Cfactor
			self._cfactor = Cfactor(self._core, self._cmd_group)
		return self._cfactor

	@property
	def gain(self):
		"""gain commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_gain'):
			from .Gain import Gain
			self._gain = Gain(self._core, self._cmd_group)
		return self._gain

	@property
	def p1Db(self):
		"""p1Db commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_p1Db'):
			from .P1Db import P1Db
			self._p1Db = P1Db(self._core, self._cmd_group)
		return self._p1Db

	@property
	def p2Db(self):
		"""p2Db commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_p2Db'):
			from .P2Db import P2Db
			self._p2Db = P2Db(self._core, self._cmd_group)
		return self._p2Db

	@property
	def p3Db(self):
		"""p3Db commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_p3Db'):
			from .P3Db import P3Db
			self._p3Db = P3Db(self._core, self._cmd_group)
		return self._p3Db

	def clone(self) -> 'Stable':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Stable(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
