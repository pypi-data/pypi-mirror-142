from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Power:
	"""Power commands group definition. 32 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("power", core, parent)

	@property
	def achannel(self):
		"""achannel commands group. 13 Sub-classes, 0 commands."""
		if not hasattr(self, '_achannel'):
			from .Achannel import Achannel
			self._achannel = Achannel(self._core, self._cmd_group)
		return self._achannel

	@property
	def bandwidth(self):
		"""bandwidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_bandwidth'):
			from .Bandwidth import Bandwidth
			self._bandwidth = Bandwidth(self._core, self._cmd_group)
		return self._bandwidth

	@property
	def ncorrection(self):
		"""ncorrection commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_ncorrection'):
			from .Ncorrection import Ncorrection
			self._ncorrection = Ncorrection(self._core, self._cmd_group)
		return self._ncorrection

	@property
	def sem(self):
		"""sem commands group. 6 Sub-classes, 0 commands."""
		if not hasattr(self, '_sem'):
			from .Sem import Sem
			self._sem = Sem(self._core, self._cmd_group)
		return self._sem

	@property
	def trace(self):
		"""trace commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trace'):
			from .Trace import Trace
			self._trace = Trace(self._core, self._cmd_group)
		return self._trace

	def clone(self) -> 'Power':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Power(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
