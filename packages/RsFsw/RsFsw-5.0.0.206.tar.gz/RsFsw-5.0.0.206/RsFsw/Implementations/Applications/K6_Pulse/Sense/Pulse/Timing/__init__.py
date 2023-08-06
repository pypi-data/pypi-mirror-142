from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Timing:
	"""Timing commands group definition. 70 total commands, 10 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("timing", core, parent)

	@property
	def dcycle(self):
		"""dcycle commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_dcycle'):
			from .Dcycle import Dcycle
			self._dcycle = Dcycle(self._core, self._cmd_group)
		return self._dcycle

	@property
	def dratio(self):
		"""dratio commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_dratio'):
			from .Dratio import Dratio
			self._dratio = Dratio(self._core, self._cmd_group)
		return self._dratio

	@property
	def fall(self):
		"""fall commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_fall'):
			from .Fall import Fall
			self._fall = Fall(self._core, self._cmd_group)
		return self._fall

	@property
	def off(self):
		"""off commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_off'):
			from .Off import Off
			self._off = Off(self._core, self._cmd_group)
		return self._off

	@property
	def prf(self):
		"""prf commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_prf'):
			from .Prf import Prf
			self._prf = Prf(self._core, self._cmd_group)
		return self._prf

	@property
	def pri(self):
		"""pri commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_pri'):
			from .Pri import Pri
			self._pri = Pri(self._core, self._cmd_group)
		return self._pri

	@property
	def pwidth(self):
		"""pwidth commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_pwidth'):
			from .Pwidth import Pwidth
			self._pwidth = Pwidth(self._core, self._cmd_group)
		return self._pwidth

	@property
	def rise(self):
		"""rise commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_rise'):
			from .Rise import Rise
			self._rise = Rise(self._core, self._cmd_group)
		return self._rise

	@property
	def settling(self):
		"""settling commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_settling'):
			from .Settling import Settling
			self._settling = Settling(self._core, self._cmd_group)
		return self._settling

	@property
	def tstamp(self):
		"""tstamp commands group. 6 Sub-classes, 1 commands."""
		if not hasattr(self, '_tstamp'):
			from .Tstamp import Tstamp
			self._tstamp = Tstamp(self._core, self._cmd_group)
		return self._tstamp

	def clone(self) -> 'Timing':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Timing(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
