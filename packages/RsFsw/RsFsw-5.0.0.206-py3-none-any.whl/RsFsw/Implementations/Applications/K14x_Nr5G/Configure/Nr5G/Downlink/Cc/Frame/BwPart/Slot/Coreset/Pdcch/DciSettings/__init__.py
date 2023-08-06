from ..............Internal.Core import Core
from ..............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DciSettings:
	"""DciSettings commands group definition. 6 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dciSettings", core, parent)

	@property
	def fdrAssign(self):
		"""fdrAssign commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fdrAssign'):
			from .FdrAssign import FdrAssign
			self._fdrAssign = FdrAssign(self._core, self._cmd_group)
		return self._fdrAssign

	@property
	def item(self):
		"""item commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_item'):
			from .Item import Item
			self._item = Item(self._core, self._cmd_group)
		return self._item

	@property
	def listPy(self):
		"""listPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_listPy'):
			from .ListPy import ListPy
			self._listPy = ListPy(self._core, self._cmd_group)
		return self._listPy

	@property
	def noBlock(self):
		"""noBlock commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_noBlock'):
			from .NoBlock import NoBlock
			self._noBlock = NoBlock(self._core, self._cmd_group)
		return self._noBlock

	@property
	def scope(self):
		"""scope commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scope'):
			from .Scope import Scope
			self._scope = Scope(self._core, self._cmd_group)
		return self._scope

	@property
	def tpcCommand(self):
		"""tpcCommand commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tpcCommand'):
			from .TpcCommand import TpcCommand
			self._tpcCommand = TpcCommand(self._core, self._cmd_group)
		return self._tpcCommand

	def clone(self) -> 'DciSettings':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DciSettings(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
