from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Status:
	"""Status commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("status", core, parent)

	@property
	def summary(self):
		"""summary commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_summary'):
			from .Summary import Summary
			self._summary = Summary(self._core, self._cmd_group)
		return self._summary

	def get(self) -> bytes:
		"""SCPI: DIAGnostic:HUMS:SYSTem:STATus \n
		Snippet: value: bytes = driver.diagnostic.hums.system.status.get() \n
		No command help available \n
			:return: system_status: No help available"""
		response = self._core.io.query_bin_block_ERROR(f'DIAGnostic:HUMS:SYSTem:STATus?')
		return response

	def clone(self) -> 'Status':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Status(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
