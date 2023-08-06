from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Aiq:
	"""Aiq commands group definition. 3 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("aiq", core, parent)

	@property
	def dcOffset(self):
		"""dcOffset commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_dcOffset'):
			from .DcOffset import DcOffset
			self._dcOffset = DcOffset(self._core, self._cmd_group)
		return self._dcOffset

	@property
	def haTiming(self):
		"""haTiming commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_haTiming'):
			from .HaTiming import HaTiming
			self._haTiming = HaTiming(self._core, self._cmd_group)
		return self._haTiming

	def clone(self) -> 'Aiq':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Aiq(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
