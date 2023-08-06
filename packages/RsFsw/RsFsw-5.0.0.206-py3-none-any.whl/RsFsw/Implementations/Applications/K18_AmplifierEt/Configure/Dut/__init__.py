from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dut:
	"""Dut commands group definition. 1 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dut", core, parent)

	@property
	def stime(self):
		"""stime commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stime'):
			from .Stime import Stime
			self._stime = Stime(self._core, self._cmd_group)
		return self._stime

	def clone(self) -> 'Dut':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dut(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
