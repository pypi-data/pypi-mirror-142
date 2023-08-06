from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	@property
	def ppdu(self):
		"""ppdu commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ppdu'):
			from .Ppdu import Ppdu
			self._ppdu = Ppdu(self._core, self._cmd_group)
		return self._ppdu

	@property
	def sc(self):
		"""sc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sc'):
			from .Sc import Sc
			self._sc = Sc(self._core, self._cmd_group)
		return self._sc

	@property
	def ru(self):
		"""ru commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ru'):
			from .Ru import Ru
			self._ru = Ru(self._core, self._cmd_group)
		return self._ru

	def clone(self) -> 'Power':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Power(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
