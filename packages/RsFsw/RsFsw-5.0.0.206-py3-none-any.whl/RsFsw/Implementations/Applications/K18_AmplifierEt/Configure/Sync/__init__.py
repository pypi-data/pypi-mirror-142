from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sync:
	"""Sync commands group definition. 8 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sync", core, parent)

	@property
	def confidence(self):
		"""confidence commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_confidence'):
			from .Confidence import Confidence
			self._confidence = Confidence(self._core, self._cmd_group)
		return self._confidence

	@property
	def domain(self):
		"""domain commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_domain'):
			from .Domain import Domain
			self._domain = Domain(self._core, self._cmd_group)
		return self._domain

	@property
	def estimation(self):
		"""estimation commands group. 4 Sub-classes, 0 commands."""
		if not hasattr(self, '_estimation'):
			from .Estimation import Estimation
			self._estimation = Estimation(self._core, self._cmd_group)
		return self._estimation

	@property
	def soFail(self):
		"""soFail commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_soFail'):
			from .SoFail import SoFail
			self._soFail = SoFail(self._core, self._cmd_group)
		return self._soFail

	@property
	def stat(self):
		"""stat commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_stat'):
			from .Stat import Stat
			self._stat = Stat(self._core, self._cmd_group)
		return self._stat

	def clone(self) -> 'Sync':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sync(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
