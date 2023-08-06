from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Display:
	"""Display commands group definition. 5 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("display", core, parent)

	@property
	def fpanel(self):
		"""fpanel commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_fpanel'):
			from .Fpanel import Fpanel
			self._fpanel = Fpanel(self._core, self._cmd_group)
		return self._fpanel

	@property
	def update(self):
		"""update commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_update'):
			from .Update import Update
			self._update = Update(self._core, self._cmd_group)
		return self._update

	@property
	def lock(self):
		"""lock commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lock'):
			from .Lock import Lock
			self._lock = Lock(self._core, self._cmd_group)
		return self._lock

	@property
	def message(self):
		"""message commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_message'):
			from .Message import Message
			self._message = Message(self._core, self._cmd_group)
		return self._message

	def clone(self) -> 'Display':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Display(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
