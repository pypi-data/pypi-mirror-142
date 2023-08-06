from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Y:
	"""Y commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("y", core, parent)

	@property
	def upper(self):
		"""upper commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_upper'):
			from .Upper import Upper
			self._upper = Upper(self._core, self._cmd_group)
		return self._upper

	@property
	def lower(self):
		"""lower commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lower'):
			from .Lower import Lower
			self._lower = Lower(self._core, self._cmd_group)
		return self._lower

	@property
	def unit(self):
		"""unit commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_unit'):
			from .Unit import Unit
			self._unit = Unit(self._core, self._cmd_group)
		return self._unit

	def clone(self) -> 'Y':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Y(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
