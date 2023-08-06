from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Demod:
	"""Demod commands group definition. 9 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("demod", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	@property
	def bestimation(self):
		"""bestimation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bestimation'):
			from .Bestimation import Bestimation
			self._bestimation = Bestimation(self._core, self._cmd_group)
		return self._bestimation

	@property
	def cbScrambling(self):
		"""cbScrambling commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbScrambling'):
			from .CbScrambling import CbScrambling
			self._cbScrambling = CbScrambling(self._core, self._cmd_group)
		return self._cbScrambling

	@property
	def cestimation(self):
		"""cestimation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cestimation'):
			from .Cestimation import Cestimation
			self._cestimation = Cestimation(self._core, self._cmd_group)
		return self._cestimation

	@property
	def daChannels(self):
		"""daChannels commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_daChannels'):
			from .DaChannels import DaChannels
			self._daChannels = DaChannels(self._core, self._cmd_group)
		return self._daChannels

	@property
	def evmCalc(self):
		"""evmCalc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_evmCalc'):
			from .EvmCalc import EvmCalc
			self._evmCalc = EvmCalc(self._core, self._cmd_group)
		return self._evmCalc

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
	def siSync(self):
		"""siSync commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_siSync'):
			from .SiSync import SiSync
			self._siSync = SiSync(self._core, self._cmd_group)
		return self._siSync

	def clone(self) -> 'Demod':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Demod(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
