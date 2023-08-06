from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fetch:
	"""Fetch commands group definition. 156 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fetch", core, parent)

	@property
	def all(self):
		"""all commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	@property
	def cc(self):
		"""cc commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cc'):
			from .Cc import Cc
			self._cc = Cc(self._core, self._cmd_group)
		return self._cc

	@property
	def taError(self):
		"""taError commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_taError'):
			from .TaError import TaError
			self._taError = TaError(self._core, self._cmd_group)
		return self._taError

	@property
	def pmeter(self):
		"""pmeter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmeter'):
			from .Pmeter import Pmeter
			self._pmeter = Pmeter(self._core, self._cmd_group)
		return self._pmeter

	def clone(self) -> 'Fetch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fetch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
