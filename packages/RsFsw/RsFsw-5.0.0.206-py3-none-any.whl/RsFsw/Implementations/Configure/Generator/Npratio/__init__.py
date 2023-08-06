from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Npratio:
	"""Npratio commands group definition. 26 total commands, 11 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("npratio", core, parent)

	@property
	def settings(self):
		"""settings commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_settings'):
			from .Settings import Settings
			self._settings = Settings(self._core, self._cmd_group)
		return self._settings

	@property
	def frequency(self):
		"""frequency commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

	@property
	def control(self):
		"""control commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_control'):
			from .Control import Control
			self._control = Control(self._core, self._cmd_group)
		return self._control

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def notch(self):
		"""notch commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_notch'):
			from .Notch import Notch
			self._notch = Notch(self._core, self._cmd_group)
		return self._notch

	@property
	def bb(self):
		"""bb commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_bb'):
			from .Bb import Bb
			self._bb = Bb(self._core, self._cmd_group)
		return self._bb

	@property
	def awgn(self):
		"""awgn commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_awgn'):
			from .Awgn import Awgn
			self._awgn = Awgn(self._core, self._cmd_group)
		return self._awgn

	@property
	def connection(self):
		"""connection commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_connection'):
			from .Connection import Connection
			self._connection = Connection(self._core, self._cmd_group)
		return self._connection

	@property
	def rfOutput(self):
		"""rfOutput commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_rfOutput'):
			from .RfOutput import RfOutput
			self._rfOutput = RfOutput(self._core, self._cmd_group)
		return self._rfOutput

	@property
	def power(self):
		"""power commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_power'):
			from .Power import Power
			self._power = Power(self._core, self._cmd_group)
		return self._power

	@property
	def external(self):
		"""external commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_external'):
			from .External import External
			self._external = External(self._core, self._cmd_group)
		return self._external

	def clone(self) -> 'Npratio':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Npratio(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
