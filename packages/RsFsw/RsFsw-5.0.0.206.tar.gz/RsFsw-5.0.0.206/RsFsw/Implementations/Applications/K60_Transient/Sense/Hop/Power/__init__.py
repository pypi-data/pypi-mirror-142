from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 20 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	@property
	def avePower(self):
		"""avePower commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_avePower'):
			from .AvePower import AvePower
			self._avePower = AvePower(self._core, self._cmd_group)
		return self._avePower

	@property
	def maxPower(self):
		"""maxPower commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_maxPower'):
			from .MaxPower import MaxPower
			self._maxPower = MaxPower(self._core, self._cmd_group)
		return self._maxPower

	@property
	def minPower(self):
		"""minPower commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_minPower'):
			from .MinPower import MinPower
			self._minPower = MinPower(self._core, self._cmd_group)
		return self._minPower

	@property
	def pwrRipple(self):
		"""pwrRipple commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_pwrRipple'):
			from .PwrRipple import PwrRipple
			self._pwrRipple = PwrRipple(self._core, self._cmd_group)
		return self._pwrRipple

	def clone(self) -> 'Power':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Power(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
