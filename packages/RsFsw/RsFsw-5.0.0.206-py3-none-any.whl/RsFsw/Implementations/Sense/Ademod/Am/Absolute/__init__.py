from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Absolute:
	"""Absolute commands group definition. 4 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("absolute", core, parent)

	@property
	def tdomain(self):
		"""tdomain commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_tdomain'):
			from .Tdomain import Tdomain
			self._tdomain = Tdomain(self._core, self._cmd_group)
		return self._tdomain

	@property
	def afSpectrum(self):
		"""afSpectrum commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_afSpectrum'):
			from .AfSpectrum import AfSpectrum
			self._afSpectrum = AfSpectrum(self._core, self._cmd_group)
		return self._afSpectrum

	def clone(self) -> 'Absolute':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Absolute(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
