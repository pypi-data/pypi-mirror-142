from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Equalizer:
	"""Equalizer commands group definition. 5 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("equalizer", core, parent)

	@property
	def filterPy(self):
		"""filterPy commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPy
			self._filterPy = FilterPy(self._core, self._cmd_group)
		return self._filterPy

	@property
	def fparameters(self):
		"""fparameters commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fparameters'):
			from .Fparameters import Fparameters
			self._fparameters = Fparameters(self._core, self._cmd_group)
		return self._fparameters

	@property
	def train(self):
		"""train commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_train'):
			from .Train import Train
			self._train = Train(self._core, self._cmd_group)
		return self._train

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def clone(self) -> 'Equalizer':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Equalizer(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
