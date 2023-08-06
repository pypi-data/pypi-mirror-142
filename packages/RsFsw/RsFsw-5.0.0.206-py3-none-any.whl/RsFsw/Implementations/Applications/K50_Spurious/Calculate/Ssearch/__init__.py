from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ssearch:
	"""Ssearch commands group definition. 1 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ssearch", core, parent)

	@property
	def table(self):
		"""table commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_table'):
			from .Table import Table
			self._table = Table(self._core, self._cmd_group)
		return self._table

	def clone(self) -> 'Ssearch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ssearch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
