from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Table:
	"""Table commands group definition. 35 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("table", core, parent)

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def timing(self):
		"""timing commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_timing'):
			from .Timing import Timing
			self._timing = Timing(self._core, self._cmd_group)
		return self._timing

	@property
	def frequency(self):
		"""frequency commands group. 10 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def fmSettling(self):
		"""fmSettling commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_fmSettling'):
			from .FmSettling import FmSettling
			self._fmSettling = FmSettling(self._core, self._cmd_group)
		return self._fmSettling

	@property
	def pmSettling(self):
		"""pmSettling commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_pmSettling'):
			from .PmSettling import PmSettling
			self._pmSettling = PmSettling(self._core, self._cmd_group)
		return self._pmSettling

	@property
	def phase(self):
		"""phase commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_phase'):
			from .Phase import Phase
			self._phase = Phase(self._core, self._cmd_group)
		return self._phase

	@property
	def power(self):
		"""power commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def results(self):
		"""results commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_results'):
			from .Results import Results
			self._results = Results(self._core, self._cmd_group)
		return self._results

	@property
	def total(self):
		"""total commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_total'):
			from .Total import Total
			self._total = Total(self._core, self._cmd_group)
		return self._total

	@property
	def column(self):
		"""column commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_column'):
			from .Column import Column
			self._column = Column(self._core, self._cmd_group)
		return self._column

	def clone(self) -> 'Table':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Table(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
