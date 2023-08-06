from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Demod:
	"""Demod commands group definition. 10 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("demod", core, parent)

	@property
	def caMode(self):
		"""caMode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_caMode'):
			from .CaMode import CaMode
			self._caMode = CaMode(self._core, self._cmd_group)
		return self._caMode

	@property
	def cestimation(self):
		"""cestimation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cestimation'):
			from .Cestimation import Cestimation
			self._cestimation = Cestimation(self._core, self._cmd_group)
		return self._cestimation

	@property
	def cetAverage(self):
		"""cetAverage commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cetAverage'):
			from .CetAverage import CetAverage
			self._cetAverage = CetAverage(self._core, self._cmd_group)
		return self._cetAverage

	@property
	def cmethod(self):
		"""cmethod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cmethod'):
			from .Cmethod import Cmethod
			self._cmethod = Cmethod(self._core, self._cmd_group)
		return self._cmethod

	@property
	def crdata(self):
		"""crdata commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crdata'):
			from .Crdata import Crdata
			self._crdata = Crdata(self._core, self._cmd_group)
		return self._crdata

	@property
	def ddata(self):
		"""ddata commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ddata'):
			from .Ddata import Ddata
			self._ddata = Ddata(self._core, self._cmd_group)
		return self._ddata

	@property
	def eflRange(self):
		"""eflRange commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eflRange'):
			from .EflRange import EflRange
			self._eflRange = EflRange(self._core, self._cmd_group)
		return self._eflRange

	@property
	def mcFilter(self):
		"""mcFilter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcFilter'):
			from .McFilter import McFilter
			self._mcFilter = McFilter(self._core, self._cmd_group)
		return self._mcFilter

	@property
	def prData(self):
		"""prData commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_prData'):
			from .PrData import PrData
			self._prData = PrData(self._core, self._cmd_group)
		return self._prData

	@property
	def stAdjust(self):
		"""stAdjust commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stAdjust'):
			from .StAdjust import StAdjust
			self._stAdjust = StAdjust(self._core, self._cmd_group)
		return self._stAdjust

	def clone(self) -> 'Demod':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Demod(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
