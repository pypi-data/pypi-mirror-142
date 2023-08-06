from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CorrectionTable:
	"""CorrectionTable commands group definition. 8 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("correctionTable", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def carrier(self):
		"""carrier commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_carrier'):
			from .Carrier import Carrier
			self._carrier = Carrier(self._core, self._cmd_group)
		return self._carrier

	@property
	def edit(self):
		"""edit commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_edit'):
			from .Edit import Edit
			self._edit = Edit(self._core, self._cmd_group)
		return self._edit

	def clone(self) -> 'CorrectionTable':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = CorrectionTable(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
