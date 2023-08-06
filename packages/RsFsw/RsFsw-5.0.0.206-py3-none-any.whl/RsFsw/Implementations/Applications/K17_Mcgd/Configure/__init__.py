from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Configure:
	"""Configure commands group definition. 30 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("configure", core, parent)

	@property
	def correctionTable(self):
		"""correctionTable commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_correctionTable'):
			from .CorrectionTable import CorrectionTable
			self._correctionTable = CorrectionTable(self._core, self._cmd_group)
		return self._correctionTable

	@property
	def generator(self):
		"""generator commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_generator'):
			from .Generator import Generator
			self._generator = Generator(self._core, self._cmd_group)
		return self._generator

	@property
	def settings(self):
		"""settings commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_settings'):
			from .Settings import Settings
			self._settings = Settings(self._core, self._cmd_group)
		return self._settings

	def clone(self) -> 'Configure':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Configure(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
