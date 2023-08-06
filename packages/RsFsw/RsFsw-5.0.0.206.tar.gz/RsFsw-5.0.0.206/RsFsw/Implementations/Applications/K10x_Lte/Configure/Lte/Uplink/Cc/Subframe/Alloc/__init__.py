from ..........Internal.Core import Core
from ..........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Alloc:
	"""Alloc commands group definition. 12 total commands, 8 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("alloc", core, parent)

	@property
	def cluster(self):
		"""cluster commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_cluster'):
			from .Cluster import Cluster
			self._cluster = Cluster(self._core, self._cmd_group)
		return self._cluster

	@property
	def cont(self):
		"""cont commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_cont'):
			from .Cont import Cont
			self._cont = Cont(self._core, self._cmd_group)
		return self._cont

	@property
	def modulation(self):
		"""modulation commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_modulation'):
			from .Modulation import Modulation
			self._modulation = Modulation(self._core, self._cmd_group)
		return self._modulation

	@property
	def precoding(self):
		"""precoding commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_precoding'):
			from .Precoding import Precoding
			self._precoding = Precoding(self._core, self._cmd_group)
		return self._precoding

	@property
	def puach(self):
		"""puach commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_puach'):
			from .Puach import Puach
			self._puach = Puach(self._core, self._cmd_group)
		return self._puach

	@property
	def pucch(self):
		"""pucch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pucch'):
			from .Pucch import Pucch
			self._pucch = Pucch(self._core, self._cmd_group)
		return self._pucch

	@property
	def pusch(self):
		"""pusch commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_pusch'):
			from .Pusch import Pusch
			self._pusch = Pusch(self._core, self._cmd_group)
		return self._pusch

	@property
	def rato(self):
		"""rato commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_rato'):
			from .Rato import Rato
			self._rato = Rato(self._core, self._cmd_group)
		return self._rato

	def clone(self) -> 'Alloc':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Alloc(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
