from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Harmonics:
	"""Harmonics commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("harmonics", core, parent)

	@property
	def identify(self):
		"""identify commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_identify'):
			from .Identify import Identify
			self._identify = Identify(self._core, self._cmd_group)
		return self._identify

	@property
	def mnumber(self):
		"""mnumber commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mnumber'):
			from .Mnumber import Mnumber
			self._mnumber = Mnumber(self._core, self._cmd_group)
		return self._mnumber

	@property
	def tolerance(self):
		"""tolerance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tolerance'):
			from .Tolerance import Tolerance
			self._tolerance = Tolerance(self._core, self._cmd_group)
		return self._tolerance

	def clone(self) -> 'Harmonics':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Harmonics(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
