from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Standard:
	"""Standard commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("standard", core, parent)

	@property
	def catalog(self):
		"""catalog commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_catalog'):
			from .Catalog import Catalog
			self._catalog = Catalog(self._core, self._cmd_group)
		return self._catalog

	@property
	def delete(self):
		"""delete commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_delete'):
			from .Delete import Delete
			self._delete = Delete(self._core, self._cmd_group)
		return self._delete

	@property
	def save(self):
		"""save commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_save'):
			from .Save import Save
			self._save = Save(self._core, self._cmd_group)
		return self._save

	def clone(self) -> 'Standard':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Standard(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
