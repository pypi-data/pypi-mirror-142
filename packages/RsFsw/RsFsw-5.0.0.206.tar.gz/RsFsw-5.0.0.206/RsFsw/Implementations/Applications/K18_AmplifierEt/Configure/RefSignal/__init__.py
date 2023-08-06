from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RefSignal:
	"""RefSignal commands group definition. 26 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("refSignal", core, parent)

	@property
	def cgw(self):
		"""cgw commands group. 3 Sub-classes, 0 commands."""
		if not hasattr(self, '_cgw'):
			from .Cgw import Cgw
			self._cgw = Cgw(self._core, self._cmd_group)
		return self._cgw

	@property
	def cwf(self):
		"""cwf commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_cwf'):
			from .Cwf import Cwf
			self._cwf = Cwf(self._core, self._cmd_group)
		return self._cwf

	@property
	def gos(self):
		"""gos commands group. 12 Sub-classes, 0 commands."""
		if not hasattr(self, '_gos'):
			from .Gos import Gos
			self._gos = Gos(self._core, self._cmd_group)
		return self._gos

	@property
	def segment(self):
		"""segment commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_segment'):
			from .Segment import Segment
			self._segment = Segment(self._core, self._cmd_group)
		return self._segment

	@property
	def sinfo(self):
		"""sinfo commands group. 5 Sub-classes, 0 commands."""
		if not hasattr(self, '_sinfo'):
			from .Sinfo import Sinfo
			self._sinfo = Sinfo(self._core, self._cmd_group)
		return self._sinfo

	def clone(self) -> 'RefSignal':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RefSignal(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
