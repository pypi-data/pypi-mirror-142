from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pspectrum:
	"""Pspectrum commands group definition. 6 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pspectrum", core, parent)

	@property
	def color(self):
		"""color commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_color'):
			from .Color import Color
			self._color = Color(self._core, self._cmd_group)
		return self._color

	def clone(self) -> 'Pspectrum':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pspectrum(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
