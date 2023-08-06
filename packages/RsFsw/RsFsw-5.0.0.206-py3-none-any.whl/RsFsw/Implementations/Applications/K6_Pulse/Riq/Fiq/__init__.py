from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fiq:
	"""Fiq commands group definition. 5 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fiq", core, parent)

	@property
	def path(self):
		"""path commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_path'):
			from .Path import Path
			self._path = Path(self._core, self._cmd_group)
		return self._path

	@property
	def window(self):
		"""window commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_window'):
			from .Window import Window
			self._window = Window(self._core, self._cmd_group)
		return self._window

	@property
	def range(self):
		"""range commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_range'):
			from .Range import Range
			self._range = Range(self._core, self._cmd_group)
		return self._range

	def clone(self) -> 'Fiq':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fiq(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
