from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Control:
	"""Control commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("control", core, parent)

	@property
	def domain(self):
		"""domain commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_domain'):
			from .Domain import Domain
			self._domain = Domain(self._core, self._cmd_group)
		return self._domain

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def offset(self):
		"""offset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_offset'):
			from .Offset import Offset
			self._offset = Offset(self._core, self._cmd_group)
		return self._offset

	@property
	def shift(self):
		"""shift commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_shift'):
			from .Shift import Shift
			self._shift = Shift(self._core, self._cmd_group)
		return self._shift

	@property
	def spacing(self):
		"""spacing commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_spacing'):
			from .Spacing import Spacing
			self._spacing = Spacing(self._core, self._cmd_group)
		return self._spacing

	def clone(self) -> 'Control':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Control(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
