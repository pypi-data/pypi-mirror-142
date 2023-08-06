from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sampling:
	"""Sampling commands group definition. 1 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sampling", core, parent)

	@property
	def clkio(self):
		"""clkio commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_clkio'):
			from .Clkio import Clkio
			self._clkio = Clkio(self._core, self._cmd_group)
		return self._clkio

	def clone(self) -> 'Sampling':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Sampling(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
