from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Edmg:
	"""Edmg commands group definition. 3 total commands, 3 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("edmg", core, parent)

	@property
	def crate(self):
		"""crate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_crate'):
			from .Crate import Crate
			self._crate = Crate(self._core, self._cmd_group)
		return self._crate

	@property
	def ncb(self):
		"""ncb commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ncb'):
			from .Ncb import Ncb
			self._ncb = Ncb(self._core, self._cmd_group)
		return self._ncb

	@property
	def ucRate(self):
		"""ucRate commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ucRate'):
			from .UcRate import UcRate
			self._ucRate = UcRate(self._core, self._cmd_group)
		return self._ucRate

	def clone(self) -> 'Edmg':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Edmg(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
