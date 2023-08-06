from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RuConfig:
	"""RuConfig commands group definition. 20 total commands, 6 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ruConfig", core, parent)

	@property
	def ehtPpdu(self):
		"""ehtPpdu commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ehtPpdu'):
			from .EhtPpdu import EhtPpdu
			self._ehtPpdu = EhtPpdu(self._core, self._cmd_group)
		return self._ehtPpdu

	@property
	def hePpdu(self):
		"""hePpdu commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hePpdu'):
			from .HePpdu import HePpdu
			self._hePpdu = HePpdu(self._core, self._cmd_group)
		return self._hePpdu

	@property
	def nheLtf(self):
		"""nheLtf commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nheLtf'):
			from .NheLtf import NheLtf
			self._nheLtf = NheLtf(self._core, self._cmd_group)
		return self._nheLtf

	@property
	def count(self):
		"""count commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_count'):
			from .Count import Count
			self._count = Count(self._core, self._cmd_group)
		return self._count

	@property
	def refresh(self):
		"""refresh commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_refresh'):
			from .Refresh import Refresh
			self._refresh = Refresh(self._core, self._cmd_group)
		return self._refresh

	@property
	def segment(self):
		"""segment commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_segment'):
			from .Segment import Segment
			self._segment = Segment(self._core, self._cmd_group)
		return self._segment

	def clone(self) -> 'RuConfig':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RuConfig(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
