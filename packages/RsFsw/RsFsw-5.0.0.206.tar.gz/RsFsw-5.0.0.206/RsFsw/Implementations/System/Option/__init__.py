from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Option:
	"""Option commands group definition. 3 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("option", core, parent)

	@property
	def trial(self):
		"""trial commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_trial'):
			from .Trial import Trial
			self._trial = Trial(self._core, self._cmd_group)
		return self._trial

	@property
	def license(self):
		"""license commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_license'):
			from .License import License
			self._license = License(self._core, self._cmd_group)
		return self._license

	def clone(self) -> 'Option':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Option(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
