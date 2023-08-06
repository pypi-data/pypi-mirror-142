from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frame:
	"""Frame commands group definition. 8 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frame", core, parent)

	@property
	def count(self):
		"""count commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Count import Count
			self._count = Count(self._core, self._cmd_group)
		return self._count

	@property
	def optimization(self):
		"""optimization commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_optimization'):
			from .Optimization import Optimization
			self._optimization = Optimization(self._core, self._cmd_group)
		return self._optimization

	@property
	def saLevel(self):
		"""saLevel commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_saLevel'):
			from .SaLevel import SaLevel
			self._saLevel = SaLevel(self._core, self._cmd_group)
		return self._saLevel

	@property
	def scount(self):
		"""scount commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scount'):
			from .Scount import Scount
			self._scount = Scount(self._core, self._cmd_group)
		return self._scount

	@property
	def slot(self):
		"""slot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_slot'):
			from .Slot import Slot
			self._slot = Slot(self._core, self._cmd_group)
		return self._slot

	@property
	def srSlot(self):
		"""srSlot commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_srSlot'):
			from .SrSlot import SrSlot
			self._srSlot = SrSlot(self._core, self._cmd_group)
		return self._srSlot

	def clone(self) -> 'Frame':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Frame(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
