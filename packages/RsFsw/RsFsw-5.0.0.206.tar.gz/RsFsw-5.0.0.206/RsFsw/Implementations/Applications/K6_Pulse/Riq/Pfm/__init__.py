from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pfm:
	"""Pfm commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pfm", core, parent)

	@property
	def width(self):
		"""width commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_width'):
			from .Width import Width
			self._width = Width(self._core, self._cmd_group)
		return self._width

	@property
	def window(self):
		"""window commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_window'):
			from .Window import Window
			self._window = Window(self._core, self._cmd_group)
		return self._window

	@property
	def coefficients(self):
		"""coefficients commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_coefficients'):
			from .Coefficients import Coefficients
			self._coefficients = Coefficients(self._core, self._cmd_group)
		return self._coefficients

	def clone(self) -> 'Pfm':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pfm(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
