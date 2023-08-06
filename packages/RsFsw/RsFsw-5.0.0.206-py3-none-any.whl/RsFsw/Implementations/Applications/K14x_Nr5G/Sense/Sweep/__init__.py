from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sweep:
	"""Sweep commands group definition. 26 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sweep", core, parent)

	@property
	def count(self):
		"""count commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Count import Count
			self._count = Count(self._core, self._cmd_group)
		return self._count

	@property
	def duration(self):
		"""duration commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_duration'):
			from .Duration import Duration
			self._duration = Duration(self._core, self._cmd_group)
		return self._duration

	@property
	def egate(self):
		"""egate commands group. 9 Sub-classes, 1 commands."""
		if not hasattr(self, '_egate'):
			from .Egate import Egate
			self._egate = Egate(self._core, self._cmd_group)
		return self._egate

	@property
	def event(self):
		"""event commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_event'):
			from .Event import Event
			self._event = Event(self._core, self._cmd_group)
		return self._event

	@property
	def lcapture(self):
		"""lcapture commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lcapture'):
			from .Lcapture import Lcapture
			self._lcapture = Lcapture(self._core, self._cmd_group)
		return self._lcapture

	@property
	def optimize(self):
		"""optimize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_optimize'):
			from .Optimize import Optimize
			self._optimize = Optimize(self._core, self._cmd_group)
		return self._optimize

	@property
	def scapture(self):
		"""scapture commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_scapture'):
			from .Scapture import Scapture
			self._scapture = Scapture(self._core, self._cmd_group)
		return self._scapture

	@property
	def time(self):
		"""time commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_time'):
			from .Time import Time
			self._time = Time(self._core, self._cmd_group)
		return self._time

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePy
			self._typePy = TypePy(self._core, self._cmd_group)
		return self._typePy

	def clone(self) -> 'Sweep':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sweep(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
