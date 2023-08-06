from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Unit:
	"""Unit commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("unit", core, parent)

	@property
	def burst(self):
		"""burst commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_burst'):
			from .Burst import Burst
			self._burst = Burst(self._core, self._cmd_group)
		return self._burst

	@property
	def evm(self):
		"""evm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_evm'):
			from .Evm import Evm
			self._evm = Evm(self._core, self._cmd_group)
		return self._evm

	@property
	def gimbalance(self):
		"""gimbalance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gimbalance'):
			from .Gimbalance import Gimbalance
			self._gimbalance = Gimbalance(self._core, self._cmd_group)
		return self._gimbalance

	@property
	def preamble(self):
		"""preamble commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_preamble'):
			from .Preamble import Preamble
			self._preamble = Preamble(self._core, self._cmd_group)
		return self._preamble

	@property
	def sflatness(self):
		"""sflatness commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sflatness'):
			from .Sflatness import Sflatness
			self._sflatness = Sflatness(self._core, self._cmd_group)
		return self._sflatness

	def clone(self) -> 'Unit':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Unit(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
