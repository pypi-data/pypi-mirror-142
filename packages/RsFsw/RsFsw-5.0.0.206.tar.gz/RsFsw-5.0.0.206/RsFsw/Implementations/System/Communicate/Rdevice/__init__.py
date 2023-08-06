from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rdevice:
	"""Rdevice commands group definition. 17 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rdevice", core, parent)

	@property
	def generator(self):
		"""generator commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_generator'):
			from .Generator import Generator
			self._generator = Generator(self._core, self._cmd_group)
		return self._generator

	@property
	def pmeter(self):
		"""pmeter commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pmeter'):
			from .Pmeter import Pmeter
			self._pmeter = Pmeter(self._core, self._cmd_group)
		return self._pmeter

	@property
	def oscilloscope(self):
		"""oscilloscope commands group. 9 Sub-classes, 0 commands."""
		if not hasattr(self, '_oscilloscope'):
			from .Oscilloscope import Oscilloscope
			self._oscilloscope = Oscilloscope(self._core, self._cmd_group)
		return self._oscilloscope

	def clone(self) -> 'Rdevice':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Rdevice(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
