from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Plc:
	"""Plc commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plc", core, parent)

	@property
	def cid(self):
		"""cid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cid'):
			from .Cid import Cid
			self._cid = Cid(self._core, self._cmd_group)
		return self._cid

	@property
	def eirp(self):
		"""eirp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eirp'):
			from .Eirp import Eirp
			self._eirp = Eirp(self._core, self._cmd_group)
		return self._eirp

	@property
	def trp(self):
		"""trp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trp'):
			from .Trp import Trp
			self._trp = Trp(self._core, self._cmd_group)
		return self._trp

	def clone(self) -> 'Plc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Plc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
