from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IfPower:
	"""IfPower commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ifPower", core, parent)

	@property
	def holdoff(self):
		"""holdoff commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_holdoff'):
			from .Holdoff import Holdoff
			self._holdoff = Holdoff(self._core, self._cmd_group)
		return self._holdoff

	@property
	def hysteresis(self):
		"""hysteresis commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hysteresis'):
			from .Hysteresis import Hysteresis
			self._hysteresis = Hysteresis(self._core, self._cmd_group)
		return self._hysteresis

	def clone(self) -> 'IfPower':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IfPower(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
