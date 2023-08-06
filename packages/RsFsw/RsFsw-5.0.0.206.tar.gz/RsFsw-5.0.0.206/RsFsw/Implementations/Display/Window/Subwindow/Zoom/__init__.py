from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Zoom:
	"""Zoom commands group definition. 4 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("zoom", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def area(self):
		"""area commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_area'):
			from .Area import Area
			self._area = Area(self._core, self._cmd_group)
		return self._area

	@property
	def multiple(self):
		"""multiple commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_multiple'):
			from .Multiple import Multiple
			self._multiple = Multiple(self._core, self._cmd_group)
		return self._multiple

	def clone(self) -> 'Zoom':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Zoom(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
