from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Estimation:
	"""Estimation commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("estimation", core, parent)

	@property
	def full(self):
		"""full commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_full'):
			from .Full import Full
			self._full = Full(self._core, self._cmd_group)
		return self._full

	@property
	def range(self):
		"""range commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_range'):
			from .Range import Range
			self._range = Range(self._core, self._cmd_group)
		return self._range

	@property
	def start(self):
		"""start commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_start'):
			from .Start import Start
			self._start = Start(self._core, self._cmd_group)
		return self._start

	@property
	def stop(self):
		"""stop commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stop'):
			from .Stop import Stop
			self._stop = Stop(self._core, self._cmd_group)
		return self._stop

	def clone(self) -> 'Estimation':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Estimation(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
