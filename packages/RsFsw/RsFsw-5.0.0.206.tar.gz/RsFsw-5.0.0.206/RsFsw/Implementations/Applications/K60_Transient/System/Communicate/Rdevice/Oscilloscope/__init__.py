from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Oscilloscope:
	"""Oscilloscope commands group definition. 10 total commands, 9 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("oscilloscope", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	@property
	def tcpip(self):
		"""tcpip commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_tcpip'):
			from .Tcpip import Tcpip
			self._tcpip = Tcpip(self._core, self._cmd_group)
		return self._tcpip

	@property
	def vdevice(self):
		"""vdevice commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vdevice'):
			from .Vdevice import Vdevice
			self._vdevice = Vdevice(self._core, self._cmd_group)
		return self._vdevice

	@property
	def vfirmware(self):
		"""vfirmware commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_vfirmware'):
			from .Vfirmware import Vfirmware
			self._vfirmware = Vfirmware(self._core, self._cmd_group)
		return self._vfirmware

	@property
	def idn(self):
		"""idn commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_idn'):
			from .Idn import Idn
			self._idn = Idn(self._core, self._cmd_group)
		return self._idn

	@property
	def ledState(self):
		"""ledState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ledState'):
			from .LedState import LedState
			self._ledState = LedState(self._core, self._cmd_group)
		return self._ledState

	@property
	def psMode(self):
		"""psMode commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_psMode'):
			from .PsMode import PsMode
			self._psMode = PsMode(self._core, self._cmd_group)
		return self._psMode

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRate
			self._symbolRate = SymbolRate(self._core, self._cmd_group)
		return self._symbolRate

	@property
	def alignment(self):
		"""alignment commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_alignment'):
			from .Alignment import Alignment
			self._alignment = Alignment(self._core, self._cmd_group)
		return self._alignment

	def clone(self) -> 'Oscilloscope':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Oscilloscope(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
