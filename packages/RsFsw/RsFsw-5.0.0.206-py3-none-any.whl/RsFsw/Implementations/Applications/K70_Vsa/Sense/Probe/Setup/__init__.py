from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Setup:
	"""Setup commands group definition. 10 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("setup", core, parent)

	@property
	def cmOffset(self):
		"""cmOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cmOffset'):
			from .CmOffset import CmOffset
			self._cmOffset = CmOffset(self._core, self._cmd_group)
		return self._cmOffset

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def pmode(self):
		"""pmode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmode'):
			from .Pmode import Pmode
			self._pmode = Pmode(self._core, self._cmd_group)
		return self._pmode

	@property
	def attRatio(self):
		"""attRatio commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_attRatio'):
			from .AttRatio import AttRatio
			self._attRatio = AttRatio(self._core, self._cmd_group)
		return self._attRatio

	@property
	def dmOffset(self):
		"""dmOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dmOffset'):
			from .DmOffset import DmOffset
			self._dmOffset = DmOffset(self._core, self._cmd_group)
		return self._dmOffset

	@property
	def pmOffset(self):
		"""pmOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmOffset'):
			from .PmOffset import PmOffset
			self._pmOffset = PmOffset(self._core, self._cmd_group)
		return self._pmOffset

	@property
	def nmOffset(self):
		"""nmOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nmOffset'):
			from .NmOffset import NmOffset
			self._nmOffset = NmOffset(self._core, self._cmd_group)
		return self._nmOffset

	@property
	def name(self):
		"""name commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_name'):
			from .Name import Name
			self._name = Name(self._core, self._cmd_group)
		return self._name

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePy
			self._typePy = TypePy(self._core, self._cmd_group)
		return self._typePy

	def clone(self) -> 'Setup':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Setup(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
