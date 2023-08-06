from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Table:
	"""Table commands group definition. 220 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("table", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def phase(self):
		"""phase commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_phase'):
			from .Phase import Phase
			self._phase = Phase(self._core, self._cmd_group)
		return self._phase

	@property
	def power(self):
		"""power commands group. 16 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def timing(self):
		"""timing commands group. 11 Sub-classes, 0 commands."""
		if not hasattr(self, '_timing'):
			from .Timing import Timing
			self._timing = Timing(self._core, self._cmd_group)
		return self._timing

	@property
	def emodel(self):
		"""emodel commands group. 11 Sub-classes, 0 commands."""
		if not hasattr(self, '_emodel'):
			from .Emodel import Emodel
			self._emodel = Emodel(self._core, self._cmd_group)
		return self._emodel

	@property
	def tsidelobe(self):
		"""tsidelobe commands group. 11 Sub-classes, 0 commands."""
		if not hasattr(self, '_tsidelobe'):
			from .Tsidelobe import Tsidelobe
			self._tsidelobe = Tsidelobe(self._core, self._cmd_group)
		return self._tsidelobe

	@property
	def all(self):
		"""all commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_all'):
			from .All import All
			self._all = All(self._core, self._cmd_group)
		return self._all

	def clone(self) -> 'Table':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Table(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
