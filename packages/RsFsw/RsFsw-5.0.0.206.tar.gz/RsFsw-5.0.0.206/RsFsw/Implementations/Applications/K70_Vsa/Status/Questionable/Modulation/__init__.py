from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modulation:
	"""Modulation commands group definition. 35 total commands, 11 Subgroups, 0 group commands
	Repeated Capability: Window, default value after init: Window.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_window_get', 'repcap_window_set', repcap.Window.Nr1)

	def repcap_window_set(self, window: repcap.Window) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to Window.Default
		Default value after init: Window.Nr1"""
		self._cmd_group.set_repcap_enum_value(window)

	def repcap_window_get(self) -> repcap.Window:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

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
	def evm(self):
		"""evm commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_evm'):
			from .Evm import Evm
			self._evm = Evm(self._core, self._cmd_group)
		return self._evm

	@property
	def phase(self):
		"""phase commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_phase'):
			from .Phase import Phase
			self._phase = Phase(self._core, self._cmd_group)
		return self._phase

	@property
	def magnitude(self):
		"""magnitude commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_magnitude'):
			from .Magnitude import Magnitude
			self._magnitude = Magnitude(self._core, self._cmd_group)
		return self._magnitude

	@property
	def cfrequency(self):
		"""cfrequency commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_cfrequency'):
			from .Cfrequency import Cfrequency
			self._cfrequency = Cfrequency(self._core, self._cmd_group)
		return self._cfrequency

	@property
	def iqRho(self):
		"""iqRho commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_iqRho'):
			from .IqRho import IqRho
			self._iqRho = IqRho(self._core, self._cmd_group)
		return self._iqRho

	@property
	def fsk(self):
		"""fsk commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_fsk'):
			from .Fsk import Fsk
			self._fsk = Fsk(self._core, self._cmd_group)
		return self._fsk

	def clone(self) -> 'Modulation':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Modulation(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
