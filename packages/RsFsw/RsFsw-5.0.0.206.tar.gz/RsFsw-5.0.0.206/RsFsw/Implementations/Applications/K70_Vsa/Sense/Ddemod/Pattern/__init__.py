from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pattern:
	"""Pattern commands group definition. 22 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	@property
	def formatPy(self):
		"""formatPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_formatPy'):
			from .FormatPy import FormatPy
			self._formatPy = FormatPy(self._core, self._cmd_group)
		return self._formatPy

	@property
	def frame(self):
		"""frame commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_frame'):
			from .Frame import Frame
			self._frame = Frame(self._core, self._cmd_group)
		return self._frame

	@property
	def ask(self):
		"""ask commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ask'):
			from .Ask import Ask
			self._ask = Ask(self._core, self._cmd_group)
		return self._ask

	@property
	def apsk(self):
		"""apsk commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_apsk'):
			from .Apsk import Apsk
			self._apsk = Apsk(self._core, self._cmd_group)
		return self._apsk

	@property
	def psk(self):
		"""psk commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_psk'):
			from .Psk import Psk
			self._psk = Psk(self._core, self._cmd_group)
		return self._psk

	@property
	def qam(self):
		"""qam commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_qam'):
			from .Qam import Qam
			self._qam = Qam(self._core, self._cmd_group)
		return self._qam

	@property
	def qpsk(self):
		"""qpsk commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_qpsk'):
			from .Qpsk import Qpsk
			self._qpsk = Qpsk(self._core, self._cmd_group)
		return self._qpsk

	@property
	def mapping(self):
		"""mapping commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_mapping'):
			from .Mapping import Mapping
			self._mapping = Mapping(self._core, self._cmd_group)
		return self._mapping

	@property
	def user(self):
		"""user commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_user'):
			from .User import User
			self._user = User(self._core, self._cmd_group)
		return self._user

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'Pattern':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Pattern(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
