from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Interleaving:
	"""Interleaving commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("interleaving", core, parent)

	@property
	def bsize(self):
		"""bsize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bsize'):
			from .Bsize import Bsize
			self._bsize = Bsize(self._core, self._cmd_group)
		return self._bsize

	@property
	def isize(self):
		"""isize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_isize'):
			from .Isize import Isize
			self._isize = Isize(self._core, self._cmd_group)
		return self._isize

	@property
	def nshift(self):
		"""nshift commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nshift'):
			from .Nshift import Nshift
			self._nshift = Nshift(self._core, self._cmd_group)
		return self._nshift

	@property
	def sindex(self):
		"""sindex commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sindex'):
			from .Sindex import Sindex
			self._sindex = Sindex(self._core, self._cmd_group)
		return self._sindex

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'Interleaving':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Interleaving(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
