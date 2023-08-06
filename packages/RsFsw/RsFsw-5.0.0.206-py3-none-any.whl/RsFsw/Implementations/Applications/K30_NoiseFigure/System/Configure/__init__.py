from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Configure:
	"""Configure commands group definition. 6 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("configure", core, parent)

	@property
	def generator(self):
		"""generator commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_generator'):
			from .Generator import Generator
			self._generator = Generator(self._core, self._cmd_group)
		return self._generator

	@property
	def dut(self):
		"""dut commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dut'):
			from .Dut import Dut
			self._dut = Dut(self._core, self._cmd_group)
		return self._dut

	def clone(self) -> 'Configure':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Configure(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
