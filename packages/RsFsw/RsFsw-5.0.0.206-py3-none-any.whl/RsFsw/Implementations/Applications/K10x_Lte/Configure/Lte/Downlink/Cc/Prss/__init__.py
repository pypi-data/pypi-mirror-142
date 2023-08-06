from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Prss:
	"""Prss commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("prss", core, parent)

	@property
	def bw(self):
		"""bw commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bw'):
			from .Bw import Bw
			self._bw = Bw(self._core, self._cmd_group)
		return self._bw

	@property
	def ci(self):
		"""ci commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ci'):
			from .Ci import Ci
			self._ci = Ci(self._core, self._cmd_group)
		return self._ci

	@property
	def nprs(self):
		"""nprs commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nprs'):
			from .Nprs import Nprs
			self._nprs = Nprs(self._core, self._cmd_group)
		return self._nprs

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'Prss':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Prss(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
