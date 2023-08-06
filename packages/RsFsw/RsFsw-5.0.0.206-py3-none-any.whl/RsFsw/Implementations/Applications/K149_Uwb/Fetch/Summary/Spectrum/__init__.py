from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Spectrum:
	"""Spectrum commands group definition. 8 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("spectrum", core, parent)

	@property
	def mask(self):
		"""mask commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_mask'):
			from .Mask import Mask
			self._mask = Mask(self._core, self._cmd_group)
		return self._mask

	@property
	def maximum(self):
		"""maximum commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_maximum'):
			from .Maximum import Maximum
			self._maximum = Maximum(self._core, self._cmd_group)
		return self._maximum

	def clone(self) -> 'Spectrum':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Spectrum(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
