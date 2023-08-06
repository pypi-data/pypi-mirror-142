from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sweep:
	"""Sweep commands group definition. 5 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sweep", core, parent)

	@property
	def count(self):
		"""count commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_count'):
			from .Count import Count
			self._count = Count(self._core, self._cmd_group)
		return self._count

	@property
	def forward(self):
		"""forward commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_forward'):
			from .Forward import Forward
			self._forward = Forward(self._core, self._cmd_group)
		return self._forward

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	@property
	def svFailed(self):
		"""svFailed commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_svFailed'):
			from .SvFailed import SvFailed
			self._svFailed = SvFailed(self._core, self._cmd_group)
		return self._svFailed

	@property
	def fhDecade(self):
		"""fhDecade commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_fhDecade'):
			from .FhDecade import FhDecade
			self._fhDecade = FhDecade(self._core, self._cmd_group)
		return self._fhDecade

	def clone(self) -> 'Sweep':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sweep(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
