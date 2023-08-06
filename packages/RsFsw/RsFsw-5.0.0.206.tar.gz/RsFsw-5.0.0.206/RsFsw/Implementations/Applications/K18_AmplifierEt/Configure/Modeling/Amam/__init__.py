from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Amam:
	"""Amam commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("amam", core, parent)

	@property
	def morder(self):
		"""morder commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_morder'):
			from .Morder import Morder
			self._morder = Morder(self._core, self._cmd_group)
		return self._morder

	@property
	def order(self):
		"""order commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_order'):
			from .Order import Order
			self._order = Order(self._core, self._cmd_group)
		return self._order

	def clone(self) -> 'Amam':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Amam(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
