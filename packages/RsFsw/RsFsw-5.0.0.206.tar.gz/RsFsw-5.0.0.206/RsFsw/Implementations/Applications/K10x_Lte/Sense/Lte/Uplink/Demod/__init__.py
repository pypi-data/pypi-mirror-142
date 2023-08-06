from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Demod:
	"""Demod commands group definition. 13 total commands, 13 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("demod", core, parent)

	@property
	def acon(self):
		"""acon commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_acon'):
			from .Acon import Acon
			self._acon = Acon(self._core, self._cmd_group)
		return self._acon

	@property
	def attSlots(self):
		"""attSlots commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_attSlots'):
			from .AttSlots import AttSlots
			self._attSlots = AttSlots(self._core, self._cmd_group)
		return self._attSlots

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	@property
	def cbScrambling(self):
		"""cbScrambling commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cbScrambling'):
			from .CbScrambling import CbScrambling
			self._cbScrambling = CbScrambling(self._core, self._cmd_group)
		return self._cbScrambling

	@property
	def cdcOffset(self):
		"""cdcOffset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cdcOffset'):
			from .CdcOffset import CdcOffset
			self._cdcOffset = CdcOffset(self._core, self._cmd_group)
		return self._cdcOffset

	@property
	def cestimation(self):
		"""cestimation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cestimation'):
			from .Cestimation import Cestimation
			self._cestimation = Cestimation(self._core, self._cmd_group)
		return self._cestimation

	@property
	def dummy(self):
		"""dummy commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_dummy'):
			from .Dummy import Dummy
			self._dummy = Dummy(self._core, self._cmd_group)
		return self._dummy

	@property
	def eePeriod(self):
		"""eePeriod commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eePeriod'):
			from .EePeriod import EePeriod
			self._eePeriod = EePeriod(self._core, self._cmd_group)
		return self._eePeriod

	@property
	def loFrequency(self):
		"""loFrequency commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_loFrequency'):
			from .LoFrequency import LoFrequency
			self._loFrequency = LoFrequency(self._core, self._cmd_group)
		return self._loFrequency

	@property
	def loLocation(self):
		"""loLocation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_loLocation'):
			from .LoLocation import LoLocation
			self._loLocation = LoLocation(self._core, self._cmd_group)
		return self._loLocation

	@property
	def mcFilter(self):
		"""mcFilter commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mcFilter'):
			from .McFilter import McFilter
			self._mcFilter = McFilter(self._core, self._cmd_group)
		return self._mcFilter

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

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
