from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Range:
	"""Range commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("range", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	@property
	def offset(self):
		"""offset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_offset'):
			from .Offset import Offset
			self._offset = Offset(self._core, self._cmd_group)
		return self._offset

	@property
	def length(self):
		"""length commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_length'):
			from .Length import Length
			self._length = Length(self._core, self._cmd_group)
		return self._length

	def clone(self) -> 'Range':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Range(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
