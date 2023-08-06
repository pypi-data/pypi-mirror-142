from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FilterPy:
	"""FilterPy commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("filterPy", core, parent)

	@property
	def yig(self):
		"""yig commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_yig'):
			from .Yig import Yig
			self._yig = Yig(self._core, self._cmd_group)
		return self._yig

	@property
	def hpass(self):
		"""hpass commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_hpass'):
			from .Hpass import Hpass
			self._hpass = Hpass(self._core, self._cmd_group)
		return self._hpass

	@property
	def saw(self):
		"""saw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_saw'):
			from .Saw import Saw
			self._saw = Saw(self._core, self._cmd_group)
		return self._saw

	def clone(self) -> 'FilterPy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = FilterPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
