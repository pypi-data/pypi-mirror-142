from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tsidelobe:
	"""Tsidelobe commands group definition. 32 total commands, 11 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tsidelobe", core, parent)

	@property
	def all(self):
		"""all commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	@property
	def psLevel(self):
		"""psLevel commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_psLevel'):
			from .PsLevel import PsLevel
			self._psLevel = PsLevel(self._core, self._cmd_group)
		return self._psLevel

	@property
	def isLevel(self):
		"""isLevel commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_isLevel'):
			from .IsLevel import IsLevel
			self._isLevel = IsLevel(self._core, self._cmd_group)
		return self._isLevel

	@property
	def mwidth(self):
		"""mwidth commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mwidth'):
			from .Mwidth import Mwidth
			self._mwidth = Mwidth(self._core, self._cmd_group)
		return self._mwidth

	@property
	def sdelay(self):
		"""sdelay commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_sdelay'):
			from .Sdelay import Sdelay
			self._sdelay = Sdelay(self._core, self._cmd_group)
		return self._sdelay

	@property
	def cratio(self):
		"""cratio commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_cratio'):
			from .Cratio import Cratio
			self._cratio = Cratio(self._core, self._cmd_group)
		return self._cratio

	@property
	def imPower(self):
		"""imPower commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_imPower'):
			from .ImPower import ImPower
			self._imPower = ImPower(self._core, self._cmd_group)
		return self._imPower

	@property
	def amPower(self):
		"""amPower commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_amPower'):
			from .AmPower import AmPower
			self._amPower = AmPower(self._core, self._cmd_group)
		return self._amPower

	@property
	def pcorrelation(self):
		"""pcorrelation commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_pcorrelation'):
			from .Pcorrelation import Pcorrelation
			self._pcorrelation = Pcorrelation(self._core, self._cmd_group)
		return self._pcorrelation

	@property
	def mphase(self):
		"""mphase commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mphase'):
			from .Mphase import Mphase
			self._mphase = Mphase(self._core, self._cmd_group)
		return self._mphase

	@property
	def mfrequency(self):
		"""mfrequency commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_mfrequency'):
			from .Mfrequency import Mfrequency
			self._mfrequency = Mfrequency(self._core, self._cmd_group)
		return self._mfrequency

	def clone(self) -> 'Tsidelobe':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tsidelobe(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
