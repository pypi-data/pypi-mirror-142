from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	@property
	def all(self):
		"""all commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	def get(self) -> int:
		"""SCPI: FETCh:BURSt:COUNt \n
		Snippet: value: int = driver.applications.k91Wlan.fetch.burst.count.get() \n
		This command returns the number of analyzed PPDUs from the current capture buffer. If multiple measurements are required
		because the number of PPDUs to analyze is greater than the number of PPDUs that can be captured in one buffer, this
		command only returns the number of captured PPDUs in the current capture buffer (as opposed to method RsFsw.Applications.
		K91_Wlan.Fetch.Burst.Count.All.get_) . \n
			:return: ppdu_count: No help available"""
		response = self._core.io.query_str(f'FETCh:BURSt:COUNt?')
		return Conversions.str_to_int(response)

	def clone(self) -> 'Count':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Count(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
