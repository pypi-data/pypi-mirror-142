from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Espectrum:
	"""Espectrum commands group definition. 5 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("espectrum", core, parent)

	@property
	def peakSearch(self):
		"""peakSearch commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_peakSearch'):
			from .PeakSearch import PeakSearch
			self._peakSearch = PeakSearch(self._core, self._cmd_group)
		return self._peakSearch

	def clone(self) -> 'Espectrum':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Espectrum(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
