from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cc:
	"""Cc commands group definition. 143 total commands, 14 Subgroups, 0 group commands
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
	def bw(self):
		"""bw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bw'):
			from .Bw import Bw
			self._bw = Bw(self._core, self._cmd_group)
		return self._bw

	@property
	def dfRange(self):
		"""dfRange commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dfRange'):
			from .DfRange import DfRange
			self._dfRange = DfRange(self._core, self._cmd_group)
		return self._dfRange

	@property
	def fnnf(self):
		"""fnnf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fnnf'):
			from .Fnnf import Fnnf
			self._fnnf = Fnnf(self._core, self._cmd_group)
		return self._fnnf

	@property
	def frame(self):
		"""frame commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_frame'):
			from .Frame import Frame
			self._frame = Frame(self._core, self._cmd_group)
		return self._frame

	@property
	def ftConfig(self):
		"""ftConfig commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ftConfig'):
			from .FtConfig import FtConfig
			self._ftConfig = FtConfig(self._core, self._cmd_group)
		return self._ftConfig

	@property
	def idc(self):
		"""idc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_idc'):
			from .Idc import Idc
			self._idc = Idc(self._core, self._cmd_group)
		return self._idc

	@property
	def pamapping(self):
		"""pamapping commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pamapping'):
			from .Pamapping import Pamapping
			self._pamapping = Pamapping(self._core, self._cmd_group)
		return self._pamapping

	@property
	def plc(self):
		"""plc commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_plc'):
			from .Plc import Plc
			self._plc = Plc(self._core, self._cmd_group)
		return self._plc

	@property
	def prach(self):
		"""prach commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_prach'):
			from .Prach import Prach
			self._prach = Prach(self._core, self._cmd_group)
		return self._prach

	@property
	def pusch(self):
		"""pusch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pusch'):
			from .Pusch import Pusch
			self._pusch = Pusch(self._core, self._cmd_group)
		return self._pusch

	@property
	def rfuc(self):
		"""rfuc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfuc'):
			from .Rfuc import Rfuc
			self._rfuc = Rfuc(self._core, self._cmd_group)
		return self._rfuc

	@property
	def rpa(self):
		"""rpa commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_rpa'):
			from .Rpa import Rpa
			self._rpa = Rpa(self._core, self._cmd_group)
		return self._rpa

	@property
	def sflatness(self):
		"""sflatness commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sflatness'):
			from .Sflatness import Sflatness
			self._sflatness = Sflatness(self._core, self._cmd_group)
		return self._sflatness

	@property
	def tprecoding(self):
		"""tprecoding commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tprecoding'):
			from .Tprecoding import Tprecoding
			self._tprecoding = Tprecoding(self._core, self._cmd_group)
		return self._tprecoding

	def clone(self) -> 'Cc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Cc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
