from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ssearch:
	"""Ssearch commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ssearch", core, parent)

	@property
	def stype(self):
		"""stype commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stype'):
			from .Stype import Stype
			self._stype = Stype(self._core, self._cmd_group)
		return self._stype

	@property
	def fplan(self):
		"""fplan commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fplan'):
			from .Fplan import Fplan
			self._fplan = Fplan(self._core, self._cmd_group)
		return self._fplan

	@property
	def rremove(self):
		"""rremove commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rremove'):
			from .Rremove import Rremove
			self._rremove = Rremove(self._core, self._cmd_group)
		return self._rremove

	@property
	def rmark(self):
		"""rmark commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rmark'):
			from .Rmark import Rmark
			self._rmark = Rmark(self._core, self._cmd_group)
		return self._rmark

	@property
	def control(self):
		"""control commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_control'):
			from .Control import Control
			self._control = Control(self._core, self._cmd_group)
		return self._control

	def clone(self) -> 'Ssearch':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ssearch(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
