from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mdpd:
	"""Mdpd commands group definition. 6 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mdpd", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def waveform(self):
		"""waveform commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_waveform'):
			from .Waveform import Waveform
			self._waveform = Waveform(self._core, self._cmd_group)
		return self._waveform

	@property
	def iteration(self):
		"""iteration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_iteration'):
			from .Iteration import Iteration
			self._iteration = Iteration(self._core, self._cmd_group)
		return self._iteration

	@property
	def order(self):
		"""order commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_order'):
			from .Order import Order
			self._order = Order(self._core, self._cmd_group)
		return self._order

	def clone(self) -> 'Mdpd':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mdpd(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
