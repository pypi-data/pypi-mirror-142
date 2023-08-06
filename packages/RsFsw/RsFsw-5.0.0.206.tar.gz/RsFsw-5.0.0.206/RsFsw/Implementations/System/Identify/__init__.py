from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Identify:
	"""Identify commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("identify", core, parent)

	@property
	def string(self):
		"""string commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_string'):
			from .String import String
			self._string = String(self._core, self._cmd_group)
		return self._string

	@property
	def factory(self):
		"""factory commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_factory'):
			from .Factory import Factory
			self._factory = Factory(self._core, self._cmd_group)
		return self._factory

	def clone(self) -> 'Identify':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Identify(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
