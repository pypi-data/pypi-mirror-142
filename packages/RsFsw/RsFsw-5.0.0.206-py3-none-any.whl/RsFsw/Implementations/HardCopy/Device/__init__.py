from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Device:
	"""Device commands group definition. 2 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("device", core, parent)

	@property
	def language(self):
		"""language commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_language'):
			from .Language import Language
			self._language = Language(self._core, self._cmd_group)
		return self._language

	@property
	def color(self):
		"""color commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_color'):
			from .Color import Color
			self._color = Color(self._core, self._cmd_group)
		return self._color

	def clone(self) -> 'Device':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Device(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
