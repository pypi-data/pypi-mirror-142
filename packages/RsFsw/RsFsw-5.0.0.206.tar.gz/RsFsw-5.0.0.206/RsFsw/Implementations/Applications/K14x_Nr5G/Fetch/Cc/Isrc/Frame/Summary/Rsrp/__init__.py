from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rsrp:
	"""Rsrp commands group definition. 6 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rsrp", core, parent)

	@property
	def csi(self):
		"""csi commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_csi'):
			from .Csi import Csi
			self._csi = Csi(self._core, self._cmd_group)
		return self._csi

	@property
	def ss(self):
		"""ss commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_ss'):
			from .Ss import Ss
			self._ss = Ss(self._core, self._cmd_group)
		return self._ss

	def clone(self) -> 'Rsrp':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rsrp(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
