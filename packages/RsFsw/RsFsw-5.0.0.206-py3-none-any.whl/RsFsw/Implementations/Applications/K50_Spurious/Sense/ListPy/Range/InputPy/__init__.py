from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InputPy:
	"""InputPy commands group definition. 3 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inputPy", core, parent)

	@property
	def attenuation(self):
		"""attenuation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_attenuation'):
			from .Attenuation import Attenuation
			self._attenuation = Attenuation(self._core, self._cmd_group)
		return self._attenuation

	@property
	def gain(self):
		"""gain commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_gain'):
			from .Gain import Gain
			self._gain = Gain(self._core, self._cmd_group)
		return self._gain

	def clone(self) -> 'InputPy':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = InputPy(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
