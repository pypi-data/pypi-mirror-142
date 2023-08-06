from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Uplink:
	"""Uplink commands group definition. 71 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("uplink", core, parent)

	@property
	def cabw(self):
		"""cabw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cabw'):
			from .Cabw import Cabw
			self._cabw = Cabw(self._core, self._cmd_group)
		return self._cabw

	@property
	def cc(self):
		"""cc commands group. 17 Sub-classes, 0 commands."""
		if not hasattr(self, '_cc'):
			from .Cc import Cc
			self._cc = Cc(self._core, self._cmd_group)
		return self._cc

	def clone(self) -> 'Uplink':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Uplink(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
