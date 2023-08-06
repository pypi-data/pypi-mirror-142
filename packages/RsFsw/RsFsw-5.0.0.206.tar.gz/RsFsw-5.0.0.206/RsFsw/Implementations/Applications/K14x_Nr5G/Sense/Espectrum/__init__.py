from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal.RepeatedCapability import RepeatedCapability
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Espectrum:
	"""Espectrum commands group definition. 49 total commands, 10 Subgroups, 0 group commands
	Repeated Capability: SubBlock, default value after init: SubBlock.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("espectrum", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_subBlock_get', 'repcap_subBlock_set', repcap.SubBlock.Nr1)

	def repcap_subBlock_set(self, subBlock: repcap.SubBlock) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SubBlock.Default
		Default value after init: SubBlock.Nr1"""
		self._cmd_group.set_repcap_enum_value(subBlock)

	def repcap_subBlock_get(self) -> repcap.SubBlock:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def bwid(self):
		"""bwid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bwid'):
			from .Bwid import Bwid
			self._bwid = Bwid(self._core, self._cmd_group)
		return self._bwid

	@property
	def filterPy(self):
		"""filterPy commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._cmd_group)
		return self._filterPy

	@property
	def hspeed(self):
		"""hspeed commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hspeed'):
			from .Hspeed import Hspeed
			self._hspeed = Hspeed(self._core, self._cmd_group)
		return self._hspeed

	@property
	def msr(self):
		"""msr commands group. 8 Sub-classes, 0 commands."""
		if not hasattr(self, '_msr'):
			from .Msr import Msr
			self._msr = Msr(self._core, self._cmd_group)
		return self._msr

	@property
	def preset(self):
		"""preset commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_preset'):
			from .Preset import Preset
			self._preset = Preset(self._core, self._cmd_group)
		return self._preset

	@property
	def range(self):
		"""range commands group. 12 Sub-classes, 1 commands."""
		if not hasattr(self, '_range'):
			from .Range import Range
			self._range = Range(self._core, self._cmd_group)
		return self._range

	@property
	def rrange(self):
		"""rrange commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rrange'):
			from .Rrange import Rrange
			self._rrange = Rrange(self._core, self._cmd_group)
		return self._rrange

	@property
	def rtype(self):
		"""rtype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rtype'):
			from .Rtype import Rtype
			self._rtype = Rtype(self._core, self._cmd_group)
		return self._rtype

	@property
	def scenter(self):
		"""scenter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scenter'):
			from .Scenter import Scenter
			self._scenter = Scenter(self._core, self._cmd_group)
		return self._scenter

	@property
	def scount(self):
		"""scount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scount'):
			from .Scount import Scount
			self._scount = Scount(self._core, self._cmd_group)
		return self._scount

	def clone(self) -> 'Espectrum':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Espectrum(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
