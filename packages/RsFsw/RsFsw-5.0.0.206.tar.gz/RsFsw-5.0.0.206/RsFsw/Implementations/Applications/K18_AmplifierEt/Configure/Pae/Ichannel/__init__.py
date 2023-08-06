from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Ichannel:
	"""Ichannel commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ichannel", core, parent)

	@property
	def multiplier(self):
		"""multiplier commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_multiplier'):
			from .Multiplier import Multiplier
			self._multiplier = Multiplier(self._core, self._cmd_group)
		return self._multiplier

	@property
	def offset(self):
		"""offset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_offset'):
			from .Offset import Offset
			self._offset = Offset(self._core, self._cmd_group)
		return self._offset

	@property
	def resistor(self):
		"""resistor commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_resistor'):
			from .Resistor import Resistor
			self._resistor = Resistor(self._core, self._cmd_group)
		return self._resistor

	def clone(self) -> 'Ichannel':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Ichannel(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
