from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Utilization:
	"""Utilization commands group definition. 5 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("utilization", core, parent)

	@property
	def history(self):
		"""history commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_history'):
			from .History import History
			self._history = History(self._core, self._cmd_group)
		return self._history

	@property
	def activity(self):
		"""activity commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_activity'):
			from .Activity import Activity
			self._activity = Activity(self._core, self._cmd_group)
		return self._activity

	def get(self) -> bytes:
		"""SCPI: DIAGnostic:HUMS:UTILization \n
		Snippet: value: bytes = driver.diagnostic.hums.utilization.get() \n
		No command help available \n
			:return: utilization: No help available"""
		response = self._core.io.query_bin_block_ERROR(f'DIAGnostic:HUMS:UTILization?')
		return response

	def clone(self) -> 'Utilization':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Utilization(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
