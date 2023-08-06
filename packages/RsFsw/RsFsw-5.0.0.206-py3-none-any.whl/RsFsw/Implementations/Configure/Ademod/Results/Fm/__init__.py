from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fm:
	"""Fm commands group definition. 4 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fm", core, parent)

	@property
	def detector(self):
		"""detector commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_detector'):
			from .Detector import Detector
			self._detector = Detector(self._core, self._cmd_group)
		return self._detector

	def clone(self) -> 'Fm':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fm(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
