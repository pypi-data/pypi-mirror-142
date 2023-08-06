from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Center:
	"""Center commands group definition. 6 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("center", core, parent)

	@property
	def cc(self):
		"""cc commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_cc'):
			from .Cc import Cc
			self._cc = Cc(self._core, self._cmd_group)
		return self._cc

	@property
	def step(self):
		"""step commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_step'):
			from .Step import Step
			self._step = Step(self._core, self._cmd_group)
		return self._step

	def clone(self) -> 'Center':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Center(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
