from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Evm:
	"""Evm commands group definition. 26 total commands, 26 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("evm", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	@property
	def ds1K(self):
		"""ds1K commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ds1K'):
			from .Ds1K import Ds1K
			self._ds1K = Ds1K(self._core, self._cmd_group)
		return self._ds1K

	@property
	def ds4K(self):
		"""ds4K commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ds4K'):
			from .Ds4K import Ds4K
			self._ds4K = Ds4K(self._core, self._cmd_group)
		return self._ds4K

	@property
	def dsqp(self):
		"""dsqp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dsqp'):
			from .Dsqp import Dsqp
			self._dsqp = Dsqp(self._core, self._cmd_group)
		return self._dsqp

	@property
	def dssf(self):
		"""dssf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dssf'):
			from .Dssf import Dssf
			self._dssf = Dssf(self._core, self._cmd_group)
		return self._dssf

	@property
	def dsst(self):
		"""dsst commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dsst'):
			from .Dsst import Dsst
			self._dsst = Dsst(self._core, self._cmd_group)
		return self._dsst

	@property
	def dsts(self):
		"""dsts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dsts'):
			from .Dsts import Dsts
			self._dsts = Dsts(self._core, self._cmd_group)
		return self._dsts

	@property
	def us1K(self):
		"""us1K commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_us1K'):
			from .Us1K import Us1K
			self._us1K = Us1K(self._core, self._cmd_group)
		return self._us1K

	@property
	def us4K(self):
		"""us4K commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_us4K'):
			from .Us4K import Us4K
			self._us4K = Us4K(self._core, self._cmd_group)
		return self._us4K

	@property
	def uspb(self):
		"""uspb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uspb'):
			from .Uspb import Uspb
			self._uspb = Uspb(self._core, self._cmd_group)
		return self._uspb

	@property
	def usqp(self):
		"""usqp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_usqp'):
			from .Usqp import Usqp
			self._usqp = Usqp(self._core, self._cmd_group)
		return self._usqp

	@property
	def usst(self):
		"""usst commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_usst'):
			from .Usst import Usst
			self._usst = Usst(self._core, self._cmd_group)
		return self._usst

	@property
	def ussf(self):
		"""ussf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ussf'):
			from .Ussf import Ussf
			self._ussf = Ussf(self._core, self._cmd_group)
		return self._ussf

	@property
	def usts(self):
		"""usts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_usts'):
			from .Usts import Usts
			self._usts = Usts(self._core, self._cmd_group)
		return self._usts

	@property
	def sd1K(self):
		"""sd1K commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sd1K'):
			from .Sd1K import Sd1K
			self._sd1K = Sd1K(self._core, self._cmd_group)
		return self._sd1K

	@property
	def sd4K(self):
		"""sd4K commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sd4K'):
			from .Sd4K import Sd4K
			self._sd4K = Sd4K(self._core, self._cmd_group)
		return self._sd4K

	@property
	def sdpb(self):
		"""sdpb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sdpb'):
			from .Sdpb import Sdpb
			self._sdpb = Sdpb(self._core, self._cmd_group)
		return self._sdpb

	@property
	def sdqp(self):
		"""sdqp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sdqp'):
			from .Sdqp import Sdqp
			self._sdqp = Sdqp(self._core, self._cmd_group)
		return self._sdqp

	@property
	def sdst(self):
		"""sdst commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sdst'):
			from .Sdst import Sdst
			self._sdst = Sdst(self._core, self._cmd_group)
		return self._sdst

	@property
	def sdsf(self):
		"""sdsf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sdsf'):
			from .Sdsf import Sdsf
			self._sdsf = Sdsf(self._core, self._cmd_group)
		return self._sdsf

	@property
	def sdts(self):
		"""sdts commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sdts'):
			from .Sdts import Sdts
			self._sdts = Sdts(self._core, self._cmd_group)
		return self._sdts

	@property
	def ucch(self):
		"""ucch commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ucch'):
			from .Ucch import Ucch
			self._ucch = Ucch(self._core, self._cmd_group)
		return self._ucch

	@property
	def uccd(self):
		"""uccd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_uccd'):
			from .Uccd import Uccd
			self._uccd = Uccd(self._core, self._cmd_group)
		return self._uccd

	@property
	def pchannel(self):
		"""pchannel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pchannel'):
			from .Pchannel import Pchannel
			self._pchannel = Pchannel(self._core, self._cmd_group)
		return self._pchannel

	@property
	def peak(self):
		"""peak commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_peak'):
			from .Peak import Peak
			self._peak = Peak(self._core, self._cmd_group)
		return self._peak

	@property
	def psignal(self):
		"""psignal commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_psignal'):
			from .Psignal import Psignal
			self._psignal = Psignal(self._core, self._cmd_group)
		return self._psignal

	def clone(self) -> 'Evm':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Evm(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
