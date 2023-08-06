from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Roscillator:
	"""Roscillator commands group definition. 10 total commands, 7 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("roscillator", core, parent)

	@property
	def source(self):
		"""source commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_source'):
			from .Source import Source
			self._source = Source(self._core, self._cmd_group)
		return self._source

	@property
	def trange(self):
		"""trange commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_trange'):
			from .Trange import Trange
			self._trange = Trange(self._core, self._cmd_group)
		return self._trange

	@property
	def lbWidth(self):
		"""lbWidth commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_lbWidth'):
			from .LbWidth import LbWidth
			self._lbWidth = LbWidth(self._core, self._cmd_group)
		return self._lbWidth

	@property
	def output(self):
		"""output commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_output'):
			from .Output import Output
			self._output = Output(self._core, self._cmd_group)
		return self._output

	@property
	def osync(self):
		"""osync commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_osync'):
			from .Osync import Osync
			self._osync = Osync(self._core, self._cmd_group)
		return self._osync

	@property
	def coupling(self):
		"""coupling commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_coupling'):
			from .Coupling import Coupling
			self._coupling = Coupling(self._core, self._cmd_group)
		return self._coupling

	@property
	def passThrough(self):
		"""passThrough commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_passThrough'):
			from .PassThrough import PassThrough
			self._passThrough = PassThrough(self._core, self._cmd_group)
		return self._passThrough

	def clone(self) -> 'Roscillator':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Roscillator(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
