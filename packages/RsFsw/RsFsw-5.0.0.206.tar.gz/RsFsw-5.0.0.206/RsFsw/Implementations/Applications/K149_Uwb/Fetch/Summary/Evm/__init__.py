from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Evm:
	"""Evm commands group definition. 28 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("evm", core, parent)

	@property
	def phr(self):
		"""phr commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_phr'):
			from .Phr import Phr
			self._phr = Phr(self._core, self._cmd_group)
		return self._phr

	@property
	def psdu(self):
		"""psdu commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_psdu'):
			from .Psdu import Psdu
			self._psdu = Psdu(self._core, self._cmd_group)
		return self._psdu

	@property
	def shr(self):
		"""shr commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_shr'):
			from .Shr import Shr
			self._shr = Shr(self._core, self._cmd_group)
		return self._shr

	@property
	def sts(self):
		"""sts commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_sts'):
			from .Sts import Sts
			self._sts = Sts(self._core, self._cmd_group)
		return self._sts

	def clone(self) -> 'Evm':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Evm(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
