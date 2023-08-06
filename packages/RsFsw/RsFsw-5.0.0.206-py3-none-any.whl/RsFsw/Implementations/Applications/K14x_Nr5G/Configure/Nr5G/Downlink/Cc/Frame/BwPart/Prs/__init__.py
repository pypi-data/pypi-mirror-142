from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prs:
	"""Prs commands group definition. 10 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prs", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def slot(self):
		"""slot commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_slot'):
			from .Slot import Slot
			self._slot = Slot(self._core, self._cmd_group)
		return self._slot

	@property
	def noRbs(self):
		"""noRbs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_noRbs'):
			from .NoRbs import NoRbs
			self._noRbs = NoRbs(self._core, self._cmd_group)
		return self._noRbs

	@property
	def srb(self):
		"""srb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_srb'):
			from .Srb import Srb
			self._srb = Srb(self._core, self._cmd_group)
		return self._srb

	@property
	def lpStart(self):
		"""lpStart commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lpStart'):
			from .LpStart import LpStart
			self._lpStart = LpStart(self._core, self._cmd_group)
		return self._lpStart

	@property
	def lprs(self):
		"""lprs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lprs'):
			from .Lprs import Lprs
			self._lprs = Lprs(self._core, self._cmd_group)
		return self._lprs

	@property
	def npId(self):
		"""npId commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_npId'):
			from .NpId import NpId
			self._npId = NpId(self._core, self._cmd_group)
		return self._npId

	@property
	def kpComb(self):
		"""kpComb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_kpComb'):
			from .KpComb import KpComb
			self._kpComb = KpComb(self._core, self._cmd_group)
		return self._kpComb

	@property
	def kpOffset(self):
		"""kpOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_kpOffset'):
			from .KpOffset import KpOffset
			self._kpOffset = KpOffset(self._core, self._cmd_group)
		return self._kpOffset

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	def clone(self) -> 'Prs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Prs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
