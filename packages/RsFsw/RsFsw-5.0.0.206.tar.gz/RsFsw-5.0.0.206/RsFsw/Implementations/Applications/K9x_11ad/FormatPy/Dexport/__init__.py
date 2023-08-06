from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dexport:
	"""Dexport commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dexport", core, parent)

	@property
	def dseparator(self):
		"""dseparator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dseparator'):
			from .Dseparator import Dseparator
			self._dseparator = Dseparator(self._core, self._cmd_group)
		return self._dseparator

	@property
	def graph(self):
		"""graph commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_graph'):
			from .Graph import Graph
			self._graph = Graph(self._core, self._cmd_group)
		return self._graph

	@property
	def header(self):
		"""header commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_header'):
			from .Header import Header
			self._header = Header(self._core, self._cmd_group)
		return self._header

	@property
	def traces(self):
		"""traces commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_traces'):
			from .Traces import Traces
			self._traces = Traces(self._core, self._cmd_group)
		return self._traces

	def clone(self) -> 'Dexport':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dexport(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
