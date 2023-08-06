from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rmev:
	"""Rmev commands group definition. 15 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rmev", core, parent)

	@property
	def avg(self):
		"""avg commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_avg'):
			from .Avg import Avg
			self._avg = Avg(self._core, self._cmd_group)
		return self._avg

	@property
	def max(self):
		"""max commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_max'):
			from .Max import Max
			self._max = Max(self._core, self._cmd_group)
		return self._max

	@property
	def min(self):
		"""min commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_min'):
			from .Min import Min
			self._min = Min(self._core, self._cmd_group)
		return self._min

	def clone(self) -> 'Rmev':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rmev(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
