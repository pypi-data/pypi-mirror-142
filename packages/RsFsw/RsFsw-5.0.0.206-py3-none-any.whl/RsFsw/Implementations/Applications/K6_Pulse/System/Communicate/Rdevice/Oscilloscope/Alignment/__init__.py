from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Alignment:
	"""Alignment commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alignment", core, parent)

	@property
	def step(self):
		"""step commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_step'):
			from .Step import Step
			self._step = Step(self._core, self._cmd_group)
		return self._step

	@property
	def falignment(self):
		"""falignment commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_falignment'):
			from .Falignment import Falignment
			self._falignment = Falignment(self._core, self._cmd_group)
		return self._falignment

	@property
	def date(self):
		"""date commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_date'):
			from .Date import Date
			self._date = Date(self._core, self._cmd_group)
		return self._date

	def clone(self) -> 'Alignment':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Alignment(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
