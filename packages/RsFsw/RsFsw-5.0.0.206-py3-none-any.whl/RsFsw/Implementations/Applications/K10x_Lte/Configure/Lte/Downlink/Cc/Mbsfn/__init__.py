from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mbsfn:
	"""Mbsfn commands group definition. 7 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mbsfn", core, parent)

	@property
	def ai(self):
		"""ai commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ai'):
			from .Ai import Ai
			self._ai = Ai(self._core, self._cmd_group)
		return self._ai

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def subframe(self):
		"""subframe commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_subframe'):
			from .Subframe import Subframe
			self._subframe = Subframe(self._core, self._cmd_group)
		return self._subframe

	def clone(self) -> 'Mbsfn':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mbsfn(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
