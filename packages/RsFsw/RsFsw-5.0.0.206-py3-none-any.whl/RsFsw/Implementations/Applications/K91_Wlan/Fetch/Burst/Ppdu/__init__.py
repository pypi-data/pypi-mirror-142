from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ppdu:
	"""Ppdu commands group definition. 5 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ppdu", core, parent)

	@property
	def evm(self):
		"""evm commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_evm'):
			from .Evm import Evm
			self._evm = Evm(self._core, self._cmd_group)
		return self._evm

	@property
	def status(self):
		"""status commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_status'):
			from .Status import Status
			self._status = Status(self._core, self._cmd_group)
		return self._status

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePy
			self._typePy = TypePy(self._core, self._cmd_group)
		return self._typePy

	def clone(self) -> 'Ppdu':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ppdu(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
