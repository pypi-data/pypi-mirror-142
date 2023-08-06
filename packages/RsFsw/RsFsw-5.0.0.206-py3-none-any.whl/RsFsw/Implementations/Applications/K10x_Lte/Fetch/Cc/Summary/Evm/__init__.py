from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Evm:
	"""Evm commands group definition. 57 total commands, 27 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("evm", core, parent)

	@property
	def all(self):
		"""all commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	@property
	def dsqp(self):
		"""dsqp commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_dsqp'):
			from .Dsqp import Dsqp
			self._dsqp = Dsqp(self._core, self._cmd_group)
		return self._dsqp

	@property
	def dssf(self):
		"""dssf commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_dssf'):
			from .Dssf import Dssf
			self._dssf = Dssf(self._core, self._cmd_group)
		return self._dssf

	@property
	def dsst(self):
		"""dsst commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_dsst'):
			from .Dsst import Dsst
			self._dsst = Dsst(self._core, self._cmd_group)
		return self._dsst

	@property
	def dsts(self):
		"""dsts commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_dsts'):
			from .Dsts import Dsts
			self._dsts = Dsts(self._core, self._cmd_group)
		return self._dsts

	@property
	def ds1K(self):
		"""ds1K commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ds1K'):
			from .Ds1K import Ds1K
			self._ds1K = Ds1K(self._core, self._cmd_group)
		return self._ds1K

	@property
	def pchannel(self):
		"""pchannel commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pchannel'):
			from .Pchannel import Pchannel
			self._pchannel = Pchannel(self._core, self._cmd_group)
		return self._pchannel

	@property
	def psignal(self):
		"""psignal commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_psignal'):
			from .Psignal import Psignal
			self._psignal = Psignal(self._core, self._cmd_group)
		return self._psignal

	@property
	def sdop(self):
		"""sdop commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sdop'):
			from .Sdop import Sdop
			self._sdop = Sdop(self._core, self._cmd_group)
		return self._sdop

	@property
	def sdqp(self):
		"""sdqp commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_sdqp'):
			from .Sdqp import Sdqp
			self._sdqp = Sdqp(self._core, self._cmd_group)
		return self._sdqp

	@property
	def sdsf(self):
		"""sdsf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sdsf'):
			from .Sdsf import Sdsf
			self._sdsf = Sdsf(self._core, self._cmd_group)
		return self._sdsf

	@property
	def sdst(self):
		"""sdst commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_sdst'):
			from .Sdst import Sdst
			self._sdst = Sdst(self._core, self._cmd_group)
		return self._sdst

	@property
	def sdts(self):
		"""sdts commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sdts'):
			from .Sdts import Sdts
			self._sdts = Sdts(self._core, self._cmd_group)
		return self._sdts

	@property
	def spop(self):
		"""spop commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_spop'):
			from .Spop import Spop
			self._spop = Spop(self._core, self._cmd_group)
		return self._spop

	@property
	def spqp(self):
		"""spqp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_spqp'):
			from .Spqp import Spqp
			self._spqp = Spqp(self._core, self._cmd_group)
		return self._spqp

	@property
	def spst(self):
		"""spst commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_spst'):
			from .Spst import Spst
			self._spst = Spst(self._core, self._cmd_group)
		return self._spst

	@property
	def uccd(self):
		"""uccd commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_uccd'):
			from .Uccd import Uccd
			self._uccd = Uccd(self._core, self._cmd_group)
		return self._uccd

	@property
	def ucch(self):
		"""ucch commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ucch'):
			from .Ucch import Ucch
			self._ucch = Ucch(self._core, self._cmd_group)
		return self._ucch

	@property
	def upop(self):
		"""upop commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_upop'):
			from .Upop import Upop
			self._upop = Upop(self._core, self._cmd_group)
		return self._upop

	@property
	def upqp(self):
		"""upqp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_upqp'):
			from .Upqp import Upqp
			self._upqp = Upqp(self._core, self._cmd_group)
		return self._upqp

	@property
	def upra(self):
		"""upra commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_upra'):
			from .Upra import Upra
			self._upra = Upra(self._core, self._cmd_group)
		return self._upra

	@property
	def upst(self):
		"""upst commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_upst'):
			from .Upst import Upst
			self._upst = Upst(self._core, self._cmd_group)
		return self._upst

	@property
	def usop(self):
		"""usop commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_usop'):
			from .Usop import Usop
			self._usop = Usop(self._core, self._cmd_group)
		return self._usop

	@property
	def usqp(self):
		"""usqp commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_usqp'):
			from .Usqp import Usqp
			self._usqp = Usqp(self._core, self._cmd_group)
		return self._usqp

	@property
	def ussf(self):
		"""ussf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ussf'):
			from .Ussf import Ussf
			self._ussf = Ussf(self._core, self._cmd_group)
		return self._ussf

	@property
	def usst(self):
		"""usst commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_usst'):
			from .Usst import Usst
			self._usst = Usst(self._core, self._cmd_group)
		return self._usst

	@property
	def usts(self):
		"""usts commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_usts'):
			from .Usts import Usts
			self._usts = Usts(self._core, self._cmd_group)
		return self._usts

	def clone(self) -> 'Evm':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Evm(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
