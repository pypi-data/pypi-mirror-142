from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ptable:
	"""Ptable commands group definition. 115 total commands, 16 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ptable", core, parent)

	@property
	def acp(self):
		"""acp commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_acp'):
			from .Acp import Acp
			self._acp = Acp(self._core, self._cmd_group)
		return self._acp

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
	def bbPower(self):
		"""bbPower commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_bbPower'):
			from .BbPower import BbPower
			self._bbPower = BbPower(self._core, self._cmd_group)
		return self._bbPower

	@property
	def cfactor(self):
		"""cfactor commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cfactor'):
			from .Cfactor import Cfactor
			self._cfactor = Cfactor(self._core, self._cmd_group)
		return self._cfactor

	@property
	def evm(self):
		"""evm commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_evm'):
			from .Evm import Evm
			self._evm = Evm(self._core, self._cmd_group)
		return self._evm

	@property
	def gain(self):
		"""gain commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gain'):
			from .Gain import Gain
			self._gain = Gain(self._core, self._cmd_group)
		return self._gain

	@property
	def icc(self):
		"""icc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_icc'):
			from .Icc import Icc
			self._icc = Icc(self._core, self._cmd_group)
		return self._icc

	@property
	def pae(self):
		"""pae commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pae'):
			from .Pae import Pae
			self._pae = Pae(self._core, self._cmd_group)
		return self._pae

	@property
	def pout(self):
		"""pout commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pout'):
			from .Pout import Pout
			self._pout = Pout(self._core, self._cmd_group)
		return self._pout

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

	@property
	def result(self):
		"""result commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_result'):
			from .Result import Result
			self._result = Result(self._core, self._cmd_group)
		return self._result

	@property
	def rms(self):
		"""rms commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rms'):
			from .Rms import Rms
			self._rms = Rms(self._core, self._cmd_group)
		return self._rms

	@property
	def vcc(self):
		"""vcc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_vcc'):
			from .Vcc import Vcc
			self._vcc = Vcc(self._core, self._cmd_group)
		return self._vcc

	def clone(self) -> 'Ptable':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ptable(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
