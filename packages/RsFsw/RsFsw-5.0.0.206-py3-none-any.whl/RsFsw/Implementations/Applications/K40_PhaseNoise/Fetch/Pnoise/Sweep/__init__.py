from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sweep:
	"""Sweep commands group definition. 7 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sweep", core, parent)

	@property
	def stop(self):
		"""stop commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stop'):
			from .Stop import Stop
			self._stop = Stop(self._core, self._cmd_group)
		return self._stop

	@property
	def symbolRate(self):
		"""symbolRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_symbolRate'):
			from .SymbolRate import SymbolRate
			self._symbolRate = SymbolRate(self._core, self._cmd_group)
		return self._symbolRate

	@property
	def avg(self):
		"""avg commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_avg'):
			from .Avg import Avg
			self._avg = Avg(self._core, self._cmd_group)
		return self._avg

	@property
	def fdrift(self):
		"""fdrift commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fdrift'):
			from .Fdrift import Fdrift
			self._fdrift = Fdrift(self._core, self._cmd_group)
		return self._fdrift

	@property
	def mdrift(self):
		"""mdrift commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mdrift'):
			from .Mdrift import Mdrift
			self._mdrift = Mdrift(self._core, self._cmd_group)
		return self._mdrift

	@property
	def ldrift(self):
		"""ldrift commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ldrift'):
			from .Ldrift import Ldrift
			self._ldrift = Ldrift(self._core, self._cmd_group)
		return self._ldrift

	@property
	def start(self):
		"""start commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_start'):
			from .Start import Start
			self._start = Start(self._core, self._cmd_group)
		return self._start

	def clone(self) -> 'Sweep':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sweep(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
