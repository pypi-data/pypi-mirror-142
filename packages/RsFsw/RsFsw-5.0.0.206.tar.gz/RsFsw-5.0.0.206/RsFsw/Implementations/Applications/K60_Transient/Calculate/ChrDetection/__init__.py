from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ChrDetection:
	"""ChrDetection commands group definition. 64 total commands, 12 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("chrDetection", core, parent)

	@property
	def compensation(self):
		"""compensation commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_compensation'):
			from .Compensation import Compensation
			self._compensation = Compensation(self._core, self._cmd_group)
		return self._compensation

	@property
	def fmTolerance(self):
		"""fmTolerance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fmTolerance'):
			from .FmTolerance import FmTolerance
			self._fmTolerance = FmTolerance(self._core, self._cmd_group)
		return self._fmTolerance

	@property
	def pmTolerance(self):
		"""pmTolerance commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_pmTolerance'):
			from .PmTolerance import PmTolerance
			self._pmTolerance = PmTolerance(self._core, self._cmd_group)
		return self._pmTolerance

	@property
	def frequency(self):
		"""frequency commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def fdeviation(self):
		"""fdeviation commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_fdeviation'):
			from .Fdeviation import Fdeviation
			self._fdeviation = Fdeviation(self._core, self._cmd_group)
		return self._fdeviation

	@property
	def pdeviation(self):
		"""pdeviation commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_pdeviation'):
			from .Pdeviation import Pdeviation
			self._pdeviation = Pdeviation(self._core, self._cmd_group)
		return self._pdeviation

	@property
	def power(self):
		"""power commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def length(self):
		"""length commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_length'):
			from .Length import Length
			self._length = Length(self._core, self._cmd_group)
		return self._length

	@property
	def states(self):
		"""states commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_states'):
			from .States import States
			self._states = States(self._core, self._cmd_group)
		return self._states

	@property
	def selected(self):
		"""selected commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_selected'):
			from .Selected import Selected
			self._selected = Selected(self._core, self._cmd_group)
		return self._selected

	@property
	def total(self):
		"""total commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_total'):
			from .Total import Total
			self._total = Total(self._core, self._cmd_group)
		return self._total

	@property
	def table(self):
		"""table commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_table'):
			from .Table import Table
			self._table = Table(self._core, self._cmd_group)
		return self._table

	def clone(self) -> 'ChrDetection':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ChrDetection(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
