from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Bandwidth:
	"""Bandwidth commands group definition. 7 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bandwidth", core, parent)

	@property
	def resolution(self):
		"""resolution commands group. 3 Sub-classes, 1 commands."""
		if not hasattr(self, '_resolution'):
			from .Resolution import Resolution
			self._resolution = Resolution(self._core, self._cmd_group)
		return self._resolution

	@property
	def video(self):
		"""video commands group. 2 Sub-classes, 1 commands."""
		if not hasattr(self, '_video'):
			from .Video import Video
			self._video = Video(self._core, self._cmd_group)
		return self._video

	def clone(self) -> 'Bandwidth':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Bandwidth(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
