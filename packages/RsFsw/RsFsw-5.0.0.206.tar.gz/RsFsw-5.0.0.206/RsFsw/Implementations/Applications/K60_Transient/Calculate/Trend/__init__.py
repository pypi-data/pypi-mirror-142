from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Trend:
	"""Trend commands group definition. 45 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("trend", core, parent)

	@property
	def hop(self):
		"""hop commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_hop'):
			from .Hop import Hop
			self._hop = Hop(self._core, self._cmd_group)
		return self._hop

	@property
	def chirp(self):
		"""chirp commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_chirp'):
			from .Chirp import Chirp
			self._chirp = Chirp(self._core, self._cmd_group)
		return self._chirp

	@property
	def x(self):
		"""x commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_x'):
			from .X import X
			self._x = X(self._core, self._cmd_group)
		return self._x

	@property
	def y(self):
		"""y commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_y'):
			from .Y import Y
			self._y = Y(self._core, self._cmd_group)
		return self._y

	@property
	def swap(self):
		"""swap commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_swap'):
			from .Swap import Swap
			self._swap = Swap(self._core, self._cmd_group)
		return self._swap

	def clone(self) -> 'Trend':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Trend(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
