from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Maximum:
	"""Maximum commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("maximum", core, parent)

	@property
	def peak(self):
		"""peak commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_peak'):
			from .Peak import Peak
			self._peak = Peak(self._core, self._cmd_group)
		return self._peak

	@property
	def above(self):
		"""above commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_above'):
			from .Above import Above
			self._above = Above(self._core, self._cmd_group)
		return self._above

	@property
	def below(self):
		"""below commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_below'):
			from .Below import Below
			self._below = Below(self._core, self._cmd_group)
		return self._below

	@property
	def next(self):
		"""next commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_next'):
			from .Next import Next
			self._next = Next(self._core, self._cmd_group)
		return self._next

	def clone(self) -> 'Maximum':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Maximum(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
