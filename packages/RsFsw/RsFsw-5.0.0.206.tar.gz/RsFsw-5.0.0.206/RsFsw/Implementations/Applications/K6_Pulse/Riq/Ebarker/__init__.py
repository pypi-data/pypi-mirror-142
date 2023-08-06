from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ebarker:
	"""Ebarker commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ebarker", core, parent)

	@property
	def width(self):
		"""width commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_width'):
			from .Width import Width
			self._width = Width(self._core, self._cmd_group)
		return self._width

	@property
	def pcode(self):
		"""pcode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcode'):
			from .Pcode import Pcode
			self._pcode = Pcode(self._core, self._cmd_group)
		return self._pcode

	@property
	def scode(self):
		"""scode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_scode'):
			from .Scode import Scode
			self._scode = Scode(self._core, self._cmd_group)
		return self._scode

	def clone(self) -> 'Ebarker':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ebarker(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
