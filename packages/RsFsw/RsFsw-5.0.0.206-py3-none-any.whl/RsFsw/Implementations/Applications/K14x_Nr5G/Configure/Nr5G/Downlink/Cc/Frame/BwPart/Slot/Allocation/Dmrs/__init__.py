from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dmrs:
	"""Dmrs commands group definition. 12 total commands, 11 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dmrs", core, parent)

	@property
	def ap(self):
		"""ap commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ap'):
			from .Ap import Ap
			self._ap = Ap(self._core, self._cmd_group)
		return self._ap

	@property
	def cgwd(self):
		"""cgwd commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cgwd'):
			from .Cgwd import Cgwd
			self._cgwd = Cgwd(self._core, self._cmd_group)
		return self._cgwd

	@property
	def ctype(self):
		"""ctype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ctype'):
			from .Ctype import Ctype
			self._ctype = Ctype(self._core, self._cmd_group)
		return self._ctype

	@property
	def msymbol(self):
		"""msymbol commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_msymbol'):
			from .Msymbol import Msymbol
			self._msymbol = Msymbol(self._core, self._cmd_group)
		return self._msymbol

	@property
	def mtype(self):
		"""mtype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mtype'):
			from .Mtype import Mtype
			self._mtype = Mtype(self._core, self._cmd_group)
		return self._mtype

	@property
	def nscid(self):
		"""nscid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nscid'):
			from .Nscid import Nscid
			self._nscid = Nscid(self._core, self._cmd_group)
		return self._nscid

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def rst(self):
		"""rst commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rst'):
			from .Rst import Rst
			self._rst = Rst(self._core, self._cmd_group)
		return self._rst

	@property
	def sgeneration(self):
		"""sgeneration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sgeneration'):
			from .Sgeneration import Sgeneration
			self._sgeneration = Sgeneration(self._core, self._cmd_group)
		return self._sgeneration

	@property
	def sid(self):
		"""sid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sid'):
			from .Sid import Sid
			self._sid = Sid(self._core, self._cmd_group)
		return self._sid

	@property
	def tapos(self):
		"""tapos commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tapos'):
			from .Tapos import Tapos
			self._tapos = Tapos(self._core, self._cmd_group)
		return self._tapos

	def clone(self) -> 'Dmrs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dmrs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
