from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AntMatrix:
	"""AntMatrix commands group definition. 8 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("antMatrix", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def address(self):
		"""address commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_address'):
			from .Address import Address
			self._address = Address(self._core, self._cmd_group)
		return self._address

	@property
	def antenna(self):
		"""antenna commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_antenna'):
			from .Antenna import Antenna
			self._antenna = Antenna(self._core, self._cmd_group)
		return self._antenna

	@property
	def refLevel(self):
		"""refLevel commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_refLevel'):
			from .RefLevel import RefLevel
			self._refLevel = RefLevel(self._core, self._cmd_group)
		return self._refLevel

	@property
	def source(self):
		"""source commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_source'):
			from .Source import Source
			self._source = Source(self._core, self._cmd_group)
		return self._source

	def clone(self) -> 'AntMatrix':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AntMatrix(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
