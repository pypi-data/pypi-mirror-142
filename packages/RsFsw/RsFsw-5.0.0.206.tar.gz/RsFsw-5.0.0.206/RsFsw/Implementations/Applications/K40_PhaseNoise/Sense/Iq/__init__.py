from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iq:
	"""Iq commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iq", core, parent)

	@property
	def tbw(self):
		"""tbw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tbw'):
			from .Tbw import Tbw
			self._tbw = Tbw(self._core, self._cmd_group)
		return self._tbw

	@property
	def dpll(self):
		"""dpll commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dpll'):
			from .Dpll import Dpll
			self._dpll = Dpll(self._core, self._cmd_group)
		return self._dpll

	@property
	def decimation(self):
		"""decimation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_decimation'):
			from .Decimation import Decimation
			self._decimation = Decimation(self._core, self._cmd_group)
		return self._decimation

	@property
	def online(self):
		"""online commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_online'):
			from .Online import Online
			self._online = Online(self._core, self._cmd_group)
		return self._online

	def clone(self) -> 'Iq':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Iq(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
