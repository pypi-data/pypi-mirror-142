from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mimo:
	"""Mimo commands group definition. 1 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mimo", core, parent)

	@property
	def antenna(self):
		"""antenna commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_antenna'):
			from .Antenna import Antenna
			self._antenna = Antenna(self._core, self._cmd_group)
		return self._antenna

	def clone(self) -> 'Mimo':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mimo(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
