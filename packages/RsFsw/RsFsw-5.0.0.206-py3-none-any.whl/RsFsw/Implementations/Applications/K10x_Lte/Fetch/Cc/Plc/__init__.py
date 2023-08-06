from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Plc:
	"""Plc commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plc", core, parent)

	@property
	def cidGroup(self):
		"""cidGroup commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cidGroup'):
			from .CidGroup import CidGroup
			self._cidGroup = CidGroup(self._core, self._cmd_group)
		return self._cidGroup

	@property
	def plid(self):
		"""plid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_plid'):
			from .Plid import Plid
			self._plid = Plid(self._core, self._cmd_group)
		return self._plid

	def clone(self) -> 'Plc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Plc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
