from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Questionable:
	"""Questionable commands group definition. 100 total commands, 20 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("questionable", core, parent)

	@property
	def event(self):
		"""event commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_event'):
			from .Event import Event
			self._event = Event(self._core, self._cmd_group)
		return self._event

	@property
	def condition(self):
		"""condition commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_condition'):
			from .Condition import Condition
			self._condition = Condition(self._core, self._cmd_group)
		return self._condition

	@property
	def enable(self):
		"""enable commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_enable'):
			from .Enable import Enable
			self._enable = Enable(self._core, self._cmd_group)
		return self._enable

	@property
	def ptransition(self):
		"""ptransition commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ptransition'):
			from .Ptransition import Ptransition
			self._ptransition = Ptransition(self._core, self._cmd_group)
		return self._ptransition

	@property
	def ntransition(self):
		"""ntransition commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ntransition'):
			from .Ntransition import Ntransition
			self._ntransition = Ntransition(self._core, self._cmd_group)
		return self._ntransition

	@property
	def power(self):
		"""power commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def limit(self):
		"""limit commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_limit'):
			from .Limit import Limit
			self._limit = Limit(self._core, self._cmd_group)
		return self._limit

	@property
	def lmargin(self):
		"""lmargin commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_lmargin'):
			from .Lmargin import Lmargin
			self._lmargin = Lmargin(self._core, self._cmd_group)
		return self._lmargin

	@property
	def acpLimit(self):
		"""acpLimit commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_acpLimit'):
			from .AcpLimit import AcpLimit
			self._acpLimit = AcpLimit(self._core, self._cmd_group)
		return self._acpLimit

	@property
	def frequency(self):
		"""frequency commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def sync(self):
		"""sync commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_sync'):
			from .Sync import Sync
			self._sync = Sync(self._core, self._cmd_group)
		return self._sync

	@property
	def diq(self):
		"""diq commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_diq'):
			from .Diq import Diq
			self._diq = Diq(self._core, self._cmd_group)
		return self._diq

	@property
	def time(self):
		"""time commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_time'):
			from .Time import Time
			self._time = Time(self._core, self._cmd_group)
		return self._time

	@property
	def transducer(self):
		"""transducer commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_transducer'):
			from .Transducer import Transducer
			self._transducer = Transducer(self._core, self._cmd_group)
		return self._transducer

	@property
	def temperature(self):
		"""temperature commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_temperature'):
			from .Temperature import Temperature
			self._temperature = Temperature(self._core, self._cmd_group)
		return self._temperature

	@property
	def pnoise(self):
		"""pnoise commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_pnoise'):
			from .Pnoise import Pnoise
			self._pnoise = Pnoise(self._core, self._cmd_group)
		return self._pnoise

	@property
	def correction(self):
		"""correction commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_correction'):
			from .Correction import Correction
			self._correction = Correction(self._core, self._cmd_group)
		return self._correction

	@property
	def extended(self):
		"""extended commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_extended'):
			from .Extended import Extended
			self._extended = Extended(self._core, self._cmd_group)
		return self._extended

	@property
	def calibration(self):
		"""calibration commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_calibration'):
			from .Calibration import Calibration
			self._calibration = Calibration(self._core, self._cmd_group)
		return self._calibration

	@property
	def integrity(self):
		"""integrity commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_integrity'):
			from .Integrity import Integrity
			self._integrity = Integrity(self._core, self._cmd_group)
		return self._integrity

	def clone(self) -> 'Questionable':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Questionable(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
