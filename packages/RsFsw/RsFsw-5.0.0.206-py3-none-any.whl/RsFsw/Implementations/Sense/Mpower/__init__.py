from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mpower:
	"""Mpower commands group definition. 4 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mpower", core, parent)

	@property
	def sequence(self):
		"""sequence commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sequence'):
			from .Sequence import Sequence
			self._sequence = Sequence(self._core, self._cmd_group)
		return self._sequence

	@property
	def ftype(self):
		"""ftype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ftype'):
			from .Ftype import Ftype
			self._ftype = Ftype(self._core, self._cmd_group)
		return self._ftype

	@property
	def result(self):
		"""result commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_result'):
			from .Result import Result
			self._result = Result(self._core, self._cmd_group)
		return self._result

	def clone(self) -> 'Mpower':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mpower(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
