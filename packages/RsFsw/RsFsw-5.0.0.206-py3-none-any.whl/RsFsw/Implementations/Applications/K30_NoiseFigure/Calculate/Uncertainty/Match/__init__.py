from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Match:
	"""Match commands group definition. 12 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("match", core, parent)

	@property
	def source(self):
		"""source commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_source'):
			from .Source import Source
			self._source = Source(self._core, self._cmd_group)
		return self._source

	@property
	def dut(self):
		"""dut commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dut'):
			from .Dut import Dut
			self._dut = Dut(self._core, self._cmd_group)
		return self._dut

	@property
	def preamp(self):
		"""preamp commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_preamp'):
			from .Preamp import Preamp
			self._preamp = Preamp(self._core, self._cmd_group)
		return self._preamp

	def clone(self) -> 'Match':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Match(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
