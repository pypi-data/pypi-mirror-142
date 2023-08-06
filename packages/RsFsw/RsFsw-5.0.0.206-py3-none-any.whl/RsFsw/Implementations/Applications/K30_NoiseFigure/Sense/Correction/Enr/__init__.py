from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Enr:
	"""Enr commands group definition. 23 total commands, 4 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("enr", core, parent)

	@property
	def calibration(self):
		"""calibration commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_calibration'):
			from .Calibration import Calibration
			self._calibration = Calibration(self._core, self._cmd_group)
		return self._calibration

	@property
	def measurement(self):
		"""measurement commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_measurement'):
			from .Measurement import Measurement
			self._measurement = Measurement(self._core, self._cmd_group)
		return self._measurement

	@property
	def common(self):
		"""common commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_common'):
			from .Common import Common
			self._common = Common(self._core, self._cmd_group)
		return self._common

	@property
	def sns(self):
		"""sns commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sns'):
			from .Sns import Sns
			self._sns = Sns(self._core, self._cmd_group)
		return self._sns

	def clone(self) -> 'Enr':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Enr(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
