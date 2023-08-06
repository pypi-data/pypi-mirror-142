from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Annotation:
	"""Annotation commands group definition. 1 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("annotation", core, parent)

	@property
	def label(self):
		"""label commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_label'):
			from .Label import Label
			self._label = Label(self._core, self._cmd_group)
		return self._label

	def clone(self) -> 'Annotation':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Annotation(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
