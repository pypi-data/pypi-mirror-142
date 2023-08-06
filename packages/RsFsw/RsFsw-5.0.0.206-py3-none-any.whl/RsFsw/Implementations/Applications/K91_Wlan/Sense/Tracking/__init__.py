from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Tracking:
	"""Tracking commands group definition. 7 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("tracking", core, parent)

	@property
	def level(self):
		"""level commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_level'):
			from .Level import Level
			self._level = Level(self._core, self._cmd_group)
		return self._level

	@property
	def phase(self):
		"""phase commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_phase'):
			from .Phase import Phase
			self._phase = Phase(self._core, self._cmd_group)
		return self._phase

	@property
	def time(self):
		"""time commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_time'):
			from .Time import Time
			self._time = Time(self._core, self._cmd_group)
		return self._time

	@property
	def pilots(self):
		"""pilots commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pilots'):
			from .Pilots import Pilots
			self._pilots = Pilots(self._core, self._cmd_group)
		return self._pilots

	@property
	def preamble(self):
		"""preamble commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_preamble'):
			from .Preamble import Preamble
			self._preamble = Preamble(self._core, self._cmd_group)
		return self._preamble

	@property
	def iqMcomp(self):
		"""iqMcomp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iqMcomp'):
			from .IqMcomp import IqMcomp
			self._iqMcomp = IqMcomp(self._core, self._cmd_group)
		return self._iqMcomp

	@property
	def crosstalk(self):
		"""crosstalk commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crosstalk'):
			from .Crosstalk import Crosstalk
			self._crosstalk = Crosstalk(self._core, self._cmd_group)
		return self._crosstalk

	def clone(self) -> 'Tracking':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Tracking(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
