from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Evaluation:
	"""Evaluation commands group definition. 9 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("evaluation", core, parent)

	@property
	def filterPy(self):
		"""filterPy commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._cmd_group)
		return self._filterPy

	@property
	def packet(self):
		"""packet commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_packet'):
			from .Packet import Packet
			self._packet = Packet(self._core, self._cmd_group)
		return self._packet

	@property
	def statistics(self):
		"""statistics commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_statistics'):
			from .Statistics import Statistics
			self._statistics = Statistics(self._core, self._cmd_group)
		return self._statistics

	def clone(self) -> 'Evaluation':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Evaluation(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
