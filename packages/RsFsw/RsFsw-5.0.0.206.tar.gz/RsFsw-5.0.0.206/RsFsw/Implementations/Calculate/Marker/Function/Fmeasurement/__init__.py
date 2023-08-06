from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fmeasurement:
	"""Fmeasurement commands group definition. 9 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fmeasurement", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def detector(self):
		"""detector commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_detector'):
			from .Detector import Detector
			self._detector = Detector(self._core, self._cmd_group)
		return self._detector

	@property
	def dwell(self):
		"""dwell commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dwell'):
			from .Dwell import Dwell
			self._dwell = Dwell(self._core, self._cmd_group)
		return self._dwell

	@property
	def result(self):
		"""result commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_result'):
			from .Result import Result
			self._result = Result(self._core, self._cmd_group)
		return self._result

	@property
	def limit(self):
		"""limit commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import Limit
			self._limit = Limit(self._core, self._cmd_group)
		return self._limit

	@property
	def peakSearch(self):
		"""peakSearch commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_peakSearch'):
			from .PeakSearch import PeakSearch
			self._peakSearch = PeakSearch(self._core, self._cmd_group)
		return self._peakSearch

	def clone(self) -> 'Fmeasurement':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Fmeasurement(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
