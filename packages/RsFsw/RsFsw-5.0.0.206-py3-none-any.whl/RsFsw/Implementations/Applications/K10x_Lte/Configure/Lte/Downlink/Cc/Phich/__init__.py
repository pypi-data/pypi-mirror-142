from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Phich:
	"""Phich commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phich", core, parent)

	@property
	def duration(self):
		"""duration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_duration'):
			from .Duration import Duration
			self._duration = Duration(self._core, self._cmd_group)
		return self._duration

	@property
	def mitm(self):
		"""mitm commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mitm'):
			from .Mitm import Mitm
			self._mitm = Mitm(self._core, self._cmd_group)
		return self._mitm

	@property
	def ngParameter(self):
		"""ngParameter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ngParameter'):
			from .NgParameter import NgParameter
			self._ngParameter = NgParameter(self._core, self._cmd_group)
		return self._ngParameter

	@property
	def noGroups(self):
		"""noGroups commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_noGroups'):
			from .NoGroups import NoGroups
			self._noGroups = NoGroups(self._core, self._cmd_group)
		return self._noGroups

	@property
	def power(self):
		"""power commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	def clone(self) -> 'Phich':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Phich(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
