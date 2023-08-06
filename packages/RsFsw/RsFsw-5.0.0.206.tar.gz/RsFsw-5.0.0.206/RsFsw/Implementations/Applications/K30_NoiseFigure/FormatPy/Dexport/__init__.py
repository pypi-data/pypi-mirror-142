from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dexport:
	"""Dexport commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dexport", core, parent)

	@property
	def cseparator(self):
		"""cseparator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cseparator'):
			from .Cseparator import Cseparator
			self._cseparator = Cseparator(self._core, self._cmd_group)
		return self._cseparator

	@property
	def dseparator(self):
		"""dseparator commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dseparator'):
			from .Dseparator import Dseparator
			self._dseparator = Dseparator(self._core, self._cmd_group)
		return self._dseparator

	@property
	def formatPy(self):
		"""formatPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPy
			self._formatPy = FormatPy(self._core, self._cmd_group)
		return self._formatPy

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
