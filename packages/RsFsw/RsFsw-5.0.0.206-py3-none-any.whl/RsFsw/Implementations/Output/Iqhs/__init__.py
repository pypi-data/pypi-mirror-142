from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Iqhs:
	"""Iqhs commands group definition. 4 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("iqhs", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRate
			self._symbolRate = SymbolRate(self._core, self._cmd_group)
		return self._symbolRate

	@property
	def cdevice(self):
		"""cdevice commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cdevice'):
			from .Cdevice import Cdevice
			self._cdevice = Cdevice(self._core, self._cmd_group)
		return self._cdevice

	@property
	def marker(self):
		"""marker commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_marker'):
			from .Marker import Marker
			self._marker = Marker(self._core, self._cmd_group)
		return self._marker

	def clone(self) -> 'Iqhs':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Iqhs(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
