from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Psweep:
	"""Psweep commands group definition. 13 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("psweep", core, parent)

	@property
	def adjust(self):
		"""adjust commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_adjust'):
			from .Adjust import Adjust
			self._adjust = Adjust(self._core, self._cmd_group)
		return self._adjust

	@property
	def expected(self):
		"""expected commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_expected'):
			from .Expected import Expected
			self._expected = Expected(self._core, self._cmd_group)
		return self._expected

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def x(self):
		"""x commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_x'):
			from .X import X
			self._x = X(self._core, self._cmd_group)
		return self._x

	@property
	def y(self):
		"""y commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_y'):
			from .Y import Y
			self._y = Y(self._core, self._cmd_group)
		return self._y

	@property
	def z(self):
		"""z commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_z'):
			from .Z import Z
			self._z = Z(self._core, self._cmd_group)
		return self._z

	def clone(self) -> 'Psweep':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Psweep(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
