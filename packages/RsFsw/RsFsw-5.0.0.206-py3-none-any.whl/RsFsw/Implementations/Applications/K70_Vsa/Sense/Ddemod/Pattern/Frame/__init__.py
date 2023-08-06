from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frame:
	"""Frame commands group definition. 10 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frame", core, parent)

	@property
	def edit(self):
		"""edit commands group. 4 Sub-classes, 2 commands."""
		if not hasattr(self, '_edit'):
			from .Edit import Edit
			self._edit = Edit(self._core, self._cmd_group)
		return self._edit

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def load(self):
		"""load commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_load'):
			from .Load import Load
			self._load = Load(self._core, self._cmd_group)
		return self._load

	def clone(self) -> 'Frame':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Frame(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
