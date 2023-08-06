from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Symbols:
	"""Symbols commands group definition. 6 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("symbols", core, parent)

	@property
	def equal(self):
		"""equal commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_equal'):
			from .Equal import Equal
			self._equal = Equal(self._core, self._cmd_group)
		return self._equal

	@property
	def min(self):
		"""min commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_min'):
			from .Min import Min
			self._min = Min(self._core, self._cmd_group)
		return self._min

	@property
	def max(self):
		"""max commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_max'):
			from .Max import Max
			self._max = Max(self._core, self._cmd_group)
		return self._max

	@property
	def offset(self):
		"""offset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_offset'):
			from .Offset import Offset
			self._offset = Offset(self._core, self._cmd_group)
		return self._offset

	@property
	def length(self):
		"""length commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_length'):
			from .Length import Length
			self._length = Length(self._core, self._cmd_group)
		return self._length

	def clone(self) -> 'Symbols':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Symbols(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
