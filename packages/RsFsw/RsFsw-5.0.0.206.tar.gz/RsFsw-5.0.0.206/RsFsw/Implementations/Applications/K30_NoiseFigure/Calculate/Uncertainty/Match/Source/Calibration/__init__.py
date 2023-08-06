from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Calibration:
	"""Calibration commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("calibration", core, parent)

	@property
	def sns(self):
		"""sns commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_sns'):
			from .Sns import Sns
			self._sns = Sns(self._core, self._cmd_group)
		return self._sns

	@property
	def vswr(self):
		"""vswr commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vswr'):
			from .Vswr import Vswr
			self._vswr = Vswr(self._core, self._cmd_group)
		return self._vswr

	@property
	def rl(self):
		"""rl commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rl'):
			from .Rl import Rl
			self._rl = Rl(self._core, self._cmd_group)
		return self._rl

	def clone(self) -> 'Calibration':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Calibration(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
