from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sanalyzer:
	"""Sanalyzer commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sanalyzer", core, parent)

	@property
	def gain(self):
		"""gain commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_gain'):
			from .Gain import Gain
			self._gain = Gain(self._core, self._cmd_group)
		return self._gain

	@property
	def noise(self):
		"""noise commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_noise'):
			from .Noise import Noise
			self._noise = Noise(self._core, self._cmd_group)
		return self._noise

	def clone(self) -> 'Sanalyzer':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sanalyzer(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
