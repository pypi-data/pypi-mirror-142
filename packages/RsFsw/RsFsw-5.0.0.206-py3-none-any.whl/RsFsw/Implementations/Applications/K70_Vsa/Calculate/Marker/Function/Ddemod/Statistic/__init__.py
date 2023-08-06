from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Statistic:
	"""Statistic commands group definition. 19 total commands, 16 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("statistic", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	@property
	def adroop(self):
		"""adroop commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_adroop'):
			from .Adroop import Adroop
			self._adroop = Adroop(self._core, self._cmd_group)
		return self._adroop

	@property
	def cfError(self):
		"""cfError commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cfError'):
			from .CfError import CfError
			self._cfError = CfError(self._core, self._cmd_group)
		return self._cfError

	@property
	def evm(self):
		"""evm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_evm'):
			from .Evm import Evm
			self._evm = Evm(self._core, self._cmd_group)
		return self._evm

	@property
	def gimbalance(self):
		"""gimbalance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gimbalance'):
			from .Gimbalance import Gimbalance
			self._gimbalance = Gimbalance(self._core, self._cmd_group)
		return self._gimbalance

	@property
	def fdError(self):
		"""fdError commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fdError'):
			from .FdError import FdError
			self._fdError = FdError(self._core, self._cmd_group)
		return self._fdError

	@property
	def iqImbalance(self):
		"""iqImbalance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iqImbalance'):
			from .IqImbalance import IqImbalance
			self._iqImbalance = IqImbalance(self._core, self._cmd_group)
		return self._iqImbalance

	@property
	def merror(self):
		"""merror commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_merror'):
			from .Merror import Merror
			self._merror = Merror(self._core, self._cmd_group)
		return self._merror

	@property
	def mpower(self):
		"""mpower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mpower'):
			from .Mpower import Mpower
			self._mpower = Mpower(self._core, self._cmd_group)
		return self._mpower

	@property
	def ooffset(self):
		"""ooffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ooffset'):
			from .Ooffset import Ooffset
			self._ooffset = Ooffset(self._core, self._cmd_group)
		return self._ooffset

	@property
	def perror(self):
		"""perror commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_perror'):
			from .Perror import Perror
			self._perror = Perror(self._core, self._cmd_group)
		return self._perror

	@property
	def qerror(self):
		"""qerror commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_qerror'):
			from .Qerror import Qerror
			self._qerror = Qerror(self._core, self._cmd_group)
		return self._qerror

	@property
	def rho(self):
		"""rho commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rho'):
			from .Rho import Rho
			self._rho = Rho(self._core, self._cmd_group)
		return self._rho

	@property
	def srError(self):
		"""srError commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_srError'):
			from .SrError import SrError
			self._srError = SrError(self._core, self._cmd_group)
		return self._srError

	@property
	def snr(self):
		"""snr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_snr'):
			from .Snr import Snr
			self._snr = Snr(self._core, self._cmd_group)
		return self._snr

	@property
	def fsk(self):
		"""fsk commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_fsk'):
			from .Fsk import Fsk
			self._fsk = Fsk(self._core, self._cmd_group)
		return self._fsk

	def clone(self) -> 'Statistic':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Statistic(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
