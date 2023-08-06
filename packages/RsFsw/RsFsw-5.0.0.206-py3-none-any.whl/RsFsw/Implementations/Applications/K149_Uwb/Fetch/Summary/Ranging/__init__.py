from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ranging:
	"""Ranging commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ranging", core, parent)

	@property
	def rmarker(self):
		"""rmarker commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rmarker'):
			from .Rmarker import Rmarker
			self._rmarker = Rmarker(self._core, self._cmd_group)
		return self._rmarker

	@property
	def srMarker(self):
		"""srMarker commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_srMarker'):
			from .SrMarker import SrMarker
			self._srMarker = SrMarker(self._core, self._cmd_group)
		return self._srMarker

	def clone(self) -> 'Ranging':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ranging(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
