from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal.RepeatedCapability import RepeatedCapability
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Csi:
	"""Csi commands group definition. 18 total commands, 15 Subgroups, 0 group commands
	Repeated Capability: CsiRs, default value after init: CsiRs.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("csi", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_csiRs_get', 'repcap_csiRs_set', repcap.CsiRs.Nr1)

	def repcap_csiRs_set(self, csiRs: repcap.CsiRs) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to CsiRs.Default
		Default value after init: CsiRs.Nr1"""
		self._cmd_group.set_repcap_enum_value(csiRs)

	def repcap_csiRs_get(self) -> repcap.CsiRs:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def bitmap(self):
		"""bitmap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bitmap'):
			from .Bitmap import Bitmap
			self._bitmap = Bitmap(self._core, self._cmd_group)
		return self._bitmap

	@property
	def ctype(self):
		"""ctype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ctype'):
			from .Ctype import Ctype
			self._ctype = Ctype(self._core, self._cmd_group)
		return self._ctype

	@property
	def density(self):
		"""density commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_density'):
			from .Density import Density
			self._density = Density(self._core, self._cmd_group)
		return self._density

	@property
	def lone(self):
		"""lone commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lone'):
			from .Lone import Lone
			self._lone = Lone(self._core, self._cmd_group)
		return self._lone

	@property
	def lzero(self):
		"""lzero commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lzero'):
			from .Lzero import Lzero
			self._lzero = Lzero(self._core, self._cmd_group)
		return self._lzero

	@property
	def noRbs(self):
		"""noRbs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_noRbs'):
			from .NoRbs import NoRbs
			self._noRbs = NoRbs(self._core, self._cmd_group)
		return self._noRbs

	@property
	def port(self):
		"""port commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_port'):
			from .Port import Port
			self._port = Port(self._core, self._cmd_group)
		return self._port

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def resources(self):
		"""resources commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_resources'):
			from .Resources import Resources
			self._resources = Resources(self._core, self._cmd_group)
		return self._resources

	@property
	def row(self):
		"""row commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_row'):
			from .Row import Row
			self._row = Row(self._core, self._cmd_group)
		return self._row

	@property
	def sid(self):
		"""sid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sid'):
			from .Sid import Sid
			self._sid = Sid(self._core, self._cmd_group)
		return self._sid

	@property
	def slot(self):
		"""slot commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_slot'):
			from .Slot import Slot
			self._slot = Slot(self._core, self._cmd_group)
		return self._slot

	@property
	def srb(self):
		"""srb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_srb'):
			from .Srb import Srb
			self._srb = Srb(self._core, self._cmd_group)
		return self._srb

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def zpower(self):
		"""zpower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_zpower'):
			from .Zpower import Zpower
			self._zpower = Zpower(self._core, self._cmd_group)
		return self._zpower

	def clone(self) -> 'Csi':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Csi(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
