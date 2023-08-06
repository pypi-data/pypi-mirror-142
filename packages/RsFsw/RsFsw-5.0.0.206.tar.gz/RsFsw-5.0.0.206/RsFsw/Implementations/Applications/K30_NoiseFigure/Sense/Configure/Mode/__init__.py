from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 4 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	@property
	def system(self):
		"""system commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_system'):
			from .System import System
			self._system = System(self._core, self._cmd_group)
		return self._system

	@property
	def dut(self):
		"""dut commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dut'):
			from .Dut import Dut
			self._dut = Dut(self._core, self._cmd_group)
		return self._dut

	def clone(self) -> 'Mode':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mode(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
