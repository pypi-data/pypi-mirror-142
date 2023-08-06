from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mcgd:
	"""Mcgd commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mcgd", core, parent)

	@property
	def correctionTable(self):
		"""correctionTable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_correctionTable'):
			from .CorrectionTable import CorrectionTable
			self._correctionTable = CorrectionTable(self._core, self._cmd_group)
		return self._correctionTable

	@property
	def meas(self):
		"""meas commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_meas'):
			from .Meas import Meas
			self._meas = Meas(self._core, self._cmd_group)
		return self._meas

	@property
	def rcalibration(self):
		"""rcalibration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rcalibration'):
			from .Rcalibration import Rcalibration
			self._rcalibration = Rcalibration(self._core, self._cmd_group)
		return self._rcalibration

	def clone(self) -> 'Mcgd':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mcgd(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
