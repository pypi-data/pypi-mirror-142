from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Dpd:
	"""Dpd commands group definition. 18 total commands, 11 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dpd", core, parent)

	@property
	def amam(self):
		"""amam commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_amam'):
			from .Amam import Amam
			self._amam = Amam(self._core, self._cmd_group)
		return self._amam

	@property
	def amxm(self):
		"""amxm commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_amxm'):
			from .Amxm import Amxm
			self._amxm = Amxm(self._core, self._cmd_group)
		return self._amxm

	@property
	def amPm(self):
		"""amPm commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_amPm'):
			from .AmPm import AmPm
			self._amPm = AmPm(self._core, self._cmd_group)
		return self._amPm

	@property
	def fname(self):
		"""fname commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fname'):
			from .Fname import Fname
			self._fname = Fname(self._core, self._cmd_group)
		return self._fname

	@property
	def file(self):
		"""file commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_file'):
			from .File import File
			self._file = File(self._core, self._cmd_group)
		return self._file

	@property
	def method(self):
		"""method commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_method'):
			from .Method import Method
			self._method = Method(self._core, self._cmd_group)
		return self._method

	@property
	def morder(self):
		"""morder commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_morder'):
			from .Morder import Morder
			self._morder = Morder(self._core, self._cmd_group)
		return self._morder

	@property
	def sequence(self):
		"""sequence commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sequence'):
			from .Sequence import Sequence
			self._sequence = Sequence(self._core, self._cmd_group)
		return self._sequence

	@property
	def shaping(self):
		"""shaping commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_shaping'):
			from .Shaping import Shaping
			self._shaping = Shaping(self._core, self._cmd_group)
		return self._shaping

	@property
	def tradeoff(self):
		"""tradeoff commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tradeoff'):
			from .Tradeoff import Tradeoff
			self._tradeoff = Tradeoff(self._core, self._cmd_group)
		return self._tradeoff

	@property
	def update(self):
		"""update commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_update'):
			from .Update import Update
			self._update = Update(self._core, self._cmd_group)
		return self._update

	def clone(self) -> 'Dpd':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Dpd(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
