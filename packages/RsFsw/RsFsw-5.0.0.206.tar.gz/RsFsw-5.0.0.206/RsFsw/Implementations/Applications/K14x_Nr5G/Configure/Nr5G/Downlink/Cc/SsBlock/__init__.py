from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal.RepeatedCapability import RepeatedCapability
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SsBlock:
	"""SsBlock commands group definition. 14 total commands, 14 Subgroups, 0 group commands
	Repeated Capability: SsBlock, default value after init: SsBlock.Nr0"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ssBlock", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_ssBlock_get', 'repcap_ssBlock_set', repcap.SsBlock.Nr0)

	def repcap_ssBlock_set(self, ssBlock: repcap.SsBlock) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to SsBlock.Default
		Default value after init: SsBlock.Nr0"""
		self._cmd_group.set_repcap_enum_value(ssBlock)

	def repcap_ssBlock_get(self) -> repcap.SsBlock:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	@property
	def asOffset(self):
		"""asOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_asOffset'):
			from .AsOffset import AsOffset
			self._asOffset = AsOffset(self._core, self._cmd_group)
		return self._asOffset

	@property
	def bsPeriod(self):
		"""bsPeriod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bsPeriod'):
			from .BsPeriod import BsPeriod
			self._bsPeriod = BsPeriod(self._core, self._cmd_group)
		return self._bsPeriod

	@property
	def detection(self):
		"""detection commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_detection'):
			from .Detection import Detection
			self._detection = Detection(self._core, self._cmd_group)
		return self._detection

	@property
	def hfOffset(self):
		"""hfOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hfOffset'):
			from .HfOffset import HfOffset
			self._hfOffset = HfOffset(self._core, self._cmd_group)
		return self._hfOffset

	@property
	def lpy(self):
		"""lpy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lpy'):
			from .Lpy import Lpy
			self._lpy = Lpy(self._core, self._cmd_group)
		return self._lpy

	@property
	def offset(self):
		"""offset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_offset'):
			from .Offset import Offset
			self._offset = Offset(self._core, self._cmd_group)
		return self._offset

	@property
	def pattern(self):
		"""pattern commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pattern'):
			from .Pattern import Pattern
			self._pattern = Pattern(self._core, self._cmd_group)
		return self._pattern

	@property
	def pbch(self):
		"""pbch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pbch'):
			from .Pbch import Pbch
			self._pbch = Pbch(self._core, self._cmd_group)
		return self._pbch

	@property
	def pdmrs(self):
		"""pdmrs commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdmrs'):
			from .Pdmrs import Pdmrs
			self._pdmrs = Pdmrs(self._core, self._cmd_group)
		return self._pdmrs

	@property
	def pss(self):
		"""pss commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_pss'):
			from .Pss import Pss
			self._pss = Pss(self._core, self._cmd_group)
		return self._pss

	@property
	def rto(self):
		"""rto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rto'):
			from .Rto import Rto
			self._rto = Rto(self._core, self._cmd_group)
		return self._rto

	@property
	def sspacing(self):
		"""sspacing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sspacing'):
			from .Sspacing import Sspacing
			self._sspacing = Sspacing(self._core, self._cmd_group)
		return self._sspacing

	@property
	def sss(self):
		"""sss commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sss'):
			from .Sss import Sss
			self._sss = Sss(self._core, self._cmd_group)
		return self._sss

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'SsBlock':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = SsBlock(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
