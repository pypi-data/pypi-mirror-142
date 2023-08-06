from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Generator:
	"""Generator commands group definition. 36 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("generator", core, parent)

	@property
	def frequency(self):
		"""frequency commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_frequency'):
			from .Frequency import Frequency
			self._frequency = Frequency(self._core, self._cmd_group)
		return self._frequency

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

	@property
	def target(self):
		"""target commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_target'):
			from .Target import Target
			self._target = Target(self._core, self._cmd_group)
		return self._target

	@property
	def npratio(self):
		"""npratio commands group. 11 Sub-classes, 0 commands."""
		if not hasattr(self, '_npratio'):
			from .Npratio import Npratio
			self._npratio = Npratio(self._core, self._cmd_group)
		return self._npratio

	@property
	def connection(self):
		"""connection commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_connection'):
			from .Connection import Connection
			self._connection = Connection(self._core, self._cmd_group)
		return self._connection

	@property
	def ipConnection(self):
		"""ipConnection commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_ipConnection'):
			from .IpConnection import IpConnection
			self._ipConnection = IpConnection(self._core, self._cmd_group)
		return self._ipConnection

	def clone(self) -> 'Generator':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Generator(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
