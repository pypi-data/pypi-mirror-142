from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Math:
	"""Math commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("math", core, parent)

	@property
	def expression(self):
		"""expression commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_expression'):
			from .Expression import Expression
			self._expression = Expression(self._core, self._cmd_group)
		return self._expression

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def position(self):
		"""position commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_position'):
			from .Position import Position
			self._position = Position(self._core, self._cmd_group)
		return self._position

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'Math':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Math(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
