from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Calibration:
	"""Calibration commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("calibration", core, parent)

	@property
	def event(self):
		"""event commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_event'):
			from .Event import Event
			self._event = Event(self._core, self._cmd_group)
		return self._event

	@property
	def condition(self):
		"""condition commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_condition'):
			from .Condition import Condition
			self._condition = Condition(self._core, self._cmd_group)
		return self._condition

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import Enable
			self._enable = Enable(self._core, self._cmd_group)
		return self._enable

	@property
	def ptransition(self):
		"""ptransition commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ptransition'):
			from .Ptransition import Ptransition
			self._ptransition = Ptransition(self._core, self._cmd_group)
		return self._ptransition

	@property
	def ntransition(self):
		"""ntransition commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ntransition'):
			from .Ntransition import Ntransition
			self._ntransition = Ntransition(self._core, self._cmd_group)
		return self._ntransition

	def clone(self) -> 'Calibration':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Calibration(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
