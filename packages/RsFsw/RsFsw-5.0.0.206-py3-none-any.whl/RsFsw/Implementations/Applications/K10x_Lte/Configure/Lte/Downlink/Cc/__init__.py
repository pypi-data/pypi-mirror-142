from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cc:
	"""Cc commands group definition. 85 total commands, 26 Subgroups, 0 group commands
	Repeated Capability: CarrierComponent, default value after init: CarrierComponent.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cc", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_carrierComponent_get', 'repcap_carrierComponent_set', repcap.CarrierComponent.Nr1)

	def repcap_carrierComponent_set(self, carrierComponent: repcap.CarrierComponent) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to CarrierComponent.Default
		Default value after init: CarrierComponent.Nr1"""
		self._cmd_group.set_repcap_enum_value(carrierComponent)

	def repcap_carrierComponent_get(self) -> repcap.CarrierComponent:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def bf(self):
		"""bf commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_bf'):
			from .Bf import Bf
			self._bf = Bf(self._core, self._cmd_group)
		return self._bf

	@property
	def bw(self):
		"""bw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bw'):
			from .Bw import Bw
			self._bw = Bw(self._core, self._cmd_group)
		return self._bw

	@property
	def csirs(self):
		"""csirs commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_csirs'):
			from .Csirs import Csirs
			self._csirs = Csirs(self._core, self._cmd_group)
		return self._csirs

	@property
	def csubframes(self):
		"""csubframes commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_csubframes'):
			from .Csubframes import Csubframes
			self._csubframes = Csubframes(self._core, self._cmd_group)
		return self._csubframes

	@property
	def cycPrefix(self):
		"""cycPrefix commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cycPrefix'):
			from .CycPrefix import CycPrefix
			self._cycPrefix = CycPrefix(self._core, self._cmd_group)
		return self._cycPrefix

	@property
	def eiNbIot(self):
		"""eiNbIot commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_eiNbIot'):
			from .EiNbIot import EiNbIot
			self._eiNbIot = EiNbIot(self._core, self._cmd_group)
		return self._eiNbIot

	@property
	def epdcch(self):
		"""epdcch commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_epdcch'):
			from .Epdcch import Epdcch
			self._epdcch = Epdcch(self._core, self._cmd_group)
		return self._epdcch

	@property
	def mbsfn(self):
		"""mbsfn commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_mbsfn'):
			from .Mbsfn import Mbsfn
			self._mbsfn = Mbsfn(self._core, self._cmd_group)
		return self._mbsfn

	@property
	def mimo(self):
		"""mimo commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_mimo'):
			from .Mimo import Mimo
			self._mimo = Mimo(self._core, self._cmd_group)
		return self._mimo

	@property
	def noRb(self):
		"""noRb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_noRb'):
			from .NoRb import NoRb
			self._noRb = NoRb(self._core, self._cmd_group)
		return self._noRb

	@property
	def nrbOffset(self):
		"""nrbOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nrbOffset'):
			from .NrbOffset import NrbOffset
			self._nrbOffset = NrbOffset(self._core, self._cmd_group)
		return self._nrbOffset

	@property
	def pbch(self):
		"""pbch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pbch'):
			from .Pbch import Pbch
			self._pbch = Pbch(self._core, self._cmd_group)
		return self._pbch

	@property
	def pcfich(self):
		"""pcfich commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pcfich'):
			from .Pcfich import Pcfich
			self._pcfich = Pcfich(self._core, self._cmd_group)
		return self._pcfich

	@property
	def pdcch(self):
		"""pdcch commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdcch'):
			from .Pdcch import Pdcch
			self._pdcch = Pdcch(self._core, self._cmd_group)
		return self._pdcch

	@property
	def pdsch(self):
		"""pdsch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdsch'):
			from .Pdsch import Pdsch
			self._pdsch = Pdsch(self._core, self._cmd_group)
		return self._pdsch

	@property
	def phich(self):
		"""phich commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_phich'):
			from .Phich import Phich
			self._phich = Phich(self._core, self._cmd_group)
		return self._phich

	@property
	def plc(self):
		"""plc commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_plc'):
			from .Plc import Plc
			self._plc = Plc(self._core, self._cmd_group)
		return self._plc

	@property
	def plci(self):
		"""plci commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_plci'):
			from .Plci import Plci
			self._plci = Plci(self._core, self._cmd_group)
		return self._plci

	@property
	def prss(self):
		"""prss commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_prss'):
			from .Prss import Prss
			self._prss = Prss(self._core, self._cmd_group)
		return self._prss

	@property
	def psOffset(self):
		"""psOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_psOffset'):
			from .PsOffset import PsOffset
			self._psOffset = PsOffset(self._core, self._cmd_group)
		return self._psOffset

	@property
	def refsig(self):
		"""refsig commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_refsig'):
			from .Refsig import Refsig
			self._refsig = Refsig(self._core, self._cmd_group)
		return self._refsig

	@property
	def sfno(self):
		"""sfno commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sfno'):
			from .Sfno import Sfno
			self._sfno = Sfno(self._core, self._cmd_group)
		return self._sfno

	@property
	def subframe(self):
		"""subframe commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_subframe'):
			from .Subframe import Subframe
			self._subframe = Subframe(self._core, self._cmd_group)
		return self._subframe

	@property
	def sync(self):
		"""sync commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_sync'):
			from .Sync import Sync
			self._sync = Sync(self._core, self._cmd_group)
		return self._sync

	@property
	def tdd(self):
		"""tdd commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tdd'):
			from .Tdd import Tdd
			self._tdd = Tdd(self._core, self._cmd_group)
		return self._tdd

	@property
	def compressed(self):
		"""compressed commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_compressed'):
			from .Compressed import Compressed
			self._compressed = Compressed(self._core, self._cmd_group)
		return self._compressed

	def clone(self) -> 'Cc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
