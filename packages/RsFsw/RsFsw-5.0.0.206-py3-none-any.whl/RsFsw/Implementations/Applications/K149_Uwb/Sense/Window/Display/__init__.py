from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Display:
	"""Display commands group definition. 8 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("display", core, parent)

	@property
	def config(self):
		"""config commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_config'):
			from .Config import Config
			self._config = Config(self._core, self._cmd_group)
		return self._config

	@property
	def rwConfig(self):
		"""rwConfig commands group. 4 Sub-classes, 1 commands."""
		if not hasattr(self, '_rwConfig'):
			from .RwConfig import RwConfig
			self._rwConfig = RwConfig(self._core, self._cmd_group)
		return self._rwConfig

	def clone(self) -> 'Display':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Display(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
