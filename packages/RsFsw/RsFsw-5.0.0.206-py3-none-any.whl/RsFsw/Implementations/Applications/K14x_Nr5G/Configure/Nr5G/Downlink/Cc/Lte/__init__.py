from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Lte:
	"""Lte commands group definition. 6 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("lte", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def pointA(self):
		"""pointA commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pointA'):
			from .PointA import PointA
			self._pointA = PointA(self._core, self._cmd_group)
		return self._pointA

	@property
	def cbw(self):
		"""cbw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbw'):
			from .Cbw import Cbw
			self._cbw = Cbw(self._core, self._cmd_group)
		return self._cbw

	@property
	def mbsfn(self):
		"""mbsfn commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mbsfn'):
			from .Mbsfn import Mbsfn
			self._mbsfn = Mbsfn(self._core, self._cmd_group)
		return self._mbsfn

	@property
	def vshift(self):
		"""vshift commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vshift'):
			from .Vshift import Vshift
			self._vshift = Vshift(self._core, self._cmd_group)
		return self._vshift

	@property
	def nap(self):
		"""nap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nap'):
			from .Nap import Nap
			self._nap = Nap(self._core, self._cmd_group)
		return self._nap

	def clone(self) -> 'Lte':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Lte(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
