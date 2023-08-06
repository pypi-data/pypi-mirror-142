from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Activity:
	"""Activity commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("activity", core, parent)

	@property
	def tracking(self):
		"""tracking commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tracking'):
			from .Tracking import Tracking
			self._tracking = Tracking(self._core, self._cmd_group)
		return self._tracking

	def get(self) -> bool:
		"""SCPI: DIAGnostic:HUMS:UTILization:ACTivity \n
		Snippet: value: bool = driver.diagnostic.hums.utilization.activity.get() \n
		No command help available \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'DIAGnostic:HUMS:UTILization:ACTivity?')
		return Conversions.str_to_bool(response)

	def clone(self) -> 'Activity':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Activity(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
