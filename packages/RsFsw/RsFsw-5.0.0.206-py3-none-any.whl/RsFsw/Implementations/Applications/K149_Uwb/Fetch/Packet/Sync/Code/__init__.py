from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Code:
	"""Code commands group definition. 4 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("code", core, parent)

	@property
	def index(self):
		"""index commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_index'):
			from .Index import Index
			self._index = Index(self._core, self._cmd_group)
		return self._index

	@property
	def length(self):
		"""length commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_length'):
			from .Length import Length
			self._length = Length(self._core, self._cmd_group)
		return self._length

	def clone(self) -> 'Code':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Code(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
