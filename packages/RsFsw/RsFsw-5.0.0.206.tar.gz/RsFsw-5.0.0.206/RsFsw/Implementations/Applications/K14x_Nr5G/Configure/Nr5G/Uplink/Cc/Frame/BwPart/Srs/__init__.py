from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Srs:
	"""Srs commands group definition. 19 total commands, 12 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("srs", core, parent)

	@property
	def fhopping(self):
		"""fhopping commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_fhopping'):
			from .Fhopping import Fhopping
			self._fhopping = Fhopping(self._core, self._cmd_group)
		return self._fhopping

	@property
	def fpos(self):
		"""fpos commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fpos'):
			from .Fpos import Fpos
			self._fpos = Fpos(self._core, self._cmd_group)
		return self._fpos

	@property
	def fshift(self):
		"""fshift commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fshift'):
			from .Fshift import Fshift
			self._fshift = Fshift(self._core, self._cmd_group)
		return self._fshift

	@property
	def nports(self):
		"""nports commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nports'):
			from .Nports import Nports
			self._nports = Nports(self._core, self._cmd_group)
		return self._nports

	@property
	def nsymbols(self):
		"""nsymbols commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nsymbols'):
			from .Nsymbols import Nsymbols
			self._nsymbols = Nsymbols(self._core, self._cmd_group)
		return self._nsymbols

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def rfactor(self):
		"""rfactor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rfactor'):
			from .Rfactor import Rfactor
			self._rfactor = Rfactor(self._core, self._cmd_group)
		return self._rfactor

	@property
	def sequence(self):
		"""sequence commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_sequence'):
			from .Sequence import Sequence
			self._sequence = Sequence(self._core, self._cmd_group)
		return self._sequence

	@property
	def slot(self):
		"""slot commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_slot'):
			from .Slot import Slot
			self._slot = Slot(self._core, self._cmd_group)
		return self._slot

	@property
	def spos(self):
		"""spos commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spos'):
			from .Spos import Spos
			self._spos = Spos(self._core, self._cmd_group)
		return self._spos

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def tcomb(self):
		"""tcomb commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tcomb'):
			from .Tcomb import Tcomb
			self._tcomb = Tcomb(self._core, self._cmd_group)
		return self._tcomb

	def clone(self) -> 'Srs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Srs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
