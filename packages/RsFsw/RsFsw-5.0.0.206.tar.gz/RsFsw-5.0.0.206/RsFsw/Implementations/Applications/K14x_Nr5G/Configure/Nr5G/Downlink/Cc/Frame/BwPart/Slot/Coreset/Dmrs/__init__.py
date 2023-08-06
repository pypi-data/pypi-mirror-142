from .............Internal.Core import Core
from .............Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dmrs:
	"""Dmrs commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dmrs", core, parent)

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def rpoint(self):
		"""rpoint commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rpoint'):
			from .Rpoint import Rpoint
			self._rpoint = Rpoint(self._core, self._cmd_group)
		return self._rpoint

	@property
	def scram(self):
		"""scram commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_scram'):
			from .Scram import Scram
			self._scram = Scram(self._core, self._cmd_group)
		return self._scram

	@property
	def sgeneration(self):
		"""sgeneration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sgeneration'):
			from .Sgeneration import Sgeneration
			self._sgeneration = Sgeneration(self._core, self._cmd_group)
		return self._sgeneration

	@property
	def sid(self):
		"""sid commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sid'):
			from .Sid import Sid
			self._sid = Sid(self._core, self._cmd_group)
		return self._sid

	def clone(self) -> 'Dmrs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dmrs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
