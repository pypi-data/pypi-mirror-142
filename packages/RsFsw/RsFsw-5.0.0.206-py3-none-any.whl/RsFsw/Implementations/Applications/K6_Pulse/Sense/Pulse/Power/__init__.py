from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 140 total commands, 16 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	@property
	def adroop(self):
		"""adroop commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_adroop'):
			from .Adroop import Adroop
			self._adroop = Adroop(self._core, self._cmd_group)
		return self._adroop

	@property
	def amplitude(self):
		"""amplitude commands group. 8 Sub-classes, 1 commands."""
		if not hasattr(self, '_amplitude'):
			from .Amplitude import Amplitude
			self._amplitude = Amplitude(self._core, self._cmd_group)
		return self._amplitude

	@property
	def ampl(self):
		"""ampl commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ampl'):
			from .Ampl import Ampl
			self._ampl = Ampl(self._core, self._cmd_group)
		return self._ampl

	@property
	def avg(self):
		"""avg commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_avg'):
			from .Avg import Avg
			self._avg = Avg(self._core, self._cmd_group)
		return self._avg

	@property
	def base(self):
		"""base commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_base'):
			from .Base import Base
			self._base = Base(self._core, self._cmd_group)
		return self._base

	@property
	def max(self):
		"""max commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_max'):
			from .Max import Max
			self._max = Max(self._core, self._cmd_group)
		return self._max

	@property
	def min(self):
		"""min commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_min'):
			from .Min import Min
			self._min = Min(self._core, self._cmd_group)
		return self._min

	@property
	def on(self):
		"""on commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_on'):
			from .On import On
			self._on = On(self._core, self._cmd_group)
		return self._on

	@property
	def overshoot(self):
		"""overshoot commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_overshoot'):
			from .Overshoot import Overshoot
			self._overshoot = Overshoot(self._core, self._cmd_group)
		return self._overshoot

	@property
	def pavg(self):
		"""pavg commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_pavg'):
			from .Pavg import Pavg
			self._pavg = Pavg(self._core, self._cmd_group)
		return self._pavg

	@property
	def pmin(self):
		"""pmin commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmin'):
			from .Pmin import Pmin
			self._pmin = Pmin(self._core, self._cmd_group)
		return self._pmin

	@property
	def point(self):
		"""point commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_point'):
			from .Point import Point
			self._point = Point(self._core, self._cmd_group)
		return self._point

	@property
	def pon(self):
		"""pon commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_pon'):
			from .Pon import Pon
			self._pon = Pon(self._core, self._cmd_group)
		return self._pon

	@property
	def ppRatio(self):
		"""ppRatio commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_ppRatio'):
			from .PpRatio import PpRatio
			self._ppRatio = PpRatio(self._core, self._cmd_group)
		return self._ppRatio

	@property
	def ripple(self):
		"""ripple commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_ripple'):
			from .Ripple import Ripple
			self._ripple = Ripple(self._core, self._cmd_group)
		return self._ripple

	@property
	def top(self):
		"""top commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_top'):
			from .Top import Top
			self._top = Top(self._core, self._cmd_group)
		return self._top

	def clone(self) -> 'Power':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Power(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
